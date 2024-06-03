import logging
import shutil
import time

from tufup.client import Client

import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QDesktopServices
from PySide6.QtNetwork import QHostAddress, QSslSocket
from PySide6.QtCore import QFile, QFileInfo, QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebSockets import QWebSocketServer

from myapp.dialog import Dialog
from myapp.core import Core
from myapp.websocketclientwrapper import WebSocketClientWrapper

import resource_rc


from myapp import settings

logger = logging.getLogger(__name__)

__version__ = settings.APP_VERSION


def progress_hook(bytes_downloaded: int, bytes_expected: int):
    progress_percent = bytes_downloaded / bytes_expected * 100
    print(f"\r{progress_percent:.1f}%", end="")
    time.sleep(0.2)  # quick and dirty: simulate slow or large download
    if progress_percent >= 100:
        print("")


def update(pre: str, skip_confirmation: bool = False):
    # Create update client
    client = Client(
        app_name=settings.APP_NAME,
        app_install_dir=settings.INSTALL_DIR,
        current_version=settings.APP_VERSION,
        metadata_dir=settings.METADATA_DIR,
        metadata_base_url=settings.METADATA_BASE_URL,
        target_dir=settings.TARGET_DIR,
        target_base_url=settings.TARGET_BASE_URL,
        refresh_required=False,
    )

    # Perform update
    new_update = client.check_for_updates(pre=pre)
    if new_update:
        # [optional] use custom metadata, if available
        if new_update.custom:
            # for example, show list of changes (see repo_add_bundle.py for definition)
            print("changes in this update:")
            for item in new_update.custom.get("changes", []):
                print(f"\t- {item}")
        # apply the update
        client.download_and_apply_update(
            skip_confirmation=skip_confirmation,
            progress_hook=progress_hook,
            # WARNING: Be very careful with `purge_dst_dir=True`, because
            # this will *irreversibly* delete *EVERYTHING* inside the
            # `app_install_dir`, except any paths specified in
            # `exclude_from_purge`. So, *ONLY* use `purge_dst_dir=True` if
            # you are absolutely certain that your `app_install_dir` does not
            # contain any unrelated content.
            purge_dst_dir=False,
            exclude_from_purge=None,
            log_file_name="install.log",
        )


def main():
    # a proper app would use argparse, but we just do minimal argument
    # parsing to keep things simple
    pre_release_channel = None
    skip_confirmation = False
    pre_release_channel = "a"
    skip_confirmation = False
    # The app must ensure dirs exist
    for dir_path in [settings.INSTALL_DIR, settings.METADATA_DIR, settings.TARGET_DIR]:
        dir_path.mkdir(exist_ok=True, parents=True)

    # The app must be shipped with a trusted "root.json" metadata file,
    # which is created using the tufup.repo tools. The app must ensure
    # this file can be found in the specified metadata_dir. The root metadata
    # file lists all trusted keys and TUF roles.
    if not settings.TRUSTED_ROOT_DST.exists():
        shutil.copy(src=settings.TRUSTED_ROOT_SRC, dst=settings.TRUSTED_ROOT_DST)
        logger.info("Trusted root metadata copied to cache.")

    # Download and apply any available updates
    update(pre=pre_release_channel, skip_confirmation=skip_confirmation)

    # Do what the app is supposed to do
    print(f"Starting {settings.APP_NAME} {settings.APP_VERSION}...")
    ...

    app = QApplication(sys.argv)
    if not QSslSocket.supportsSsl():
        print("The example requires SSL support.")
        sys.exit(-1)
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    js_file_info = QFileInfo(f"{cur_dir}/qwebchannel.js")
    if not js_file_info.exists():
        QFile.copy(":/qtwebchannel/qwebchannel.js", js_file_info.absoluteFilePath())

    # setup the QWebSocketServer
    server = QWebSocketServer(
        "QWebChannel Standalone Example Server", QWebSocketServer.NonSecureMode
    )
    if not server.listen(QHostAddress.LocalHost, 12345):
        print("Failed to open web socket server.")
        sys.exit(-1)

    # wrap WebSocket clients in QWebChannelAbstractTransport objects
    client_wrapper = WebSocketClientWrapper(server)

    # setup the channel
    channel = QWebChannel()
    client_wrapper.client_connected.connect(channel.connectTo)

    # setup the UI
    dialog = Dialog()

    # setup the core and publish it to the QWebChannel
    core = Core(dialog)
    channel.registerObject("core", core)

    # open a browser window with the client HTML page
    url = QUrl.fromLocalFile(f"{cur_dir}/index.html")
    QDesktopServices.openUrl(url)

    display_url = url.toDisplayString()
    message = f"Initialization complete, opening browser at {display_url}."
    dialog.display_message(message)
    dialog.show()

    sys.exit(app.exec())

    ...

    print("Done.")


if __name__ == "__main__":
    main(sys.argv[1:])
