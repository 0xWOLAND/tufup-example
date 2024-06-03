from PySide6.QtCore import QObject, Signal, Slot


class Core(QObject):
    """An instance of this class gets published over the WebChannel and is then
    accessible to HTML clients."""

    sendText = Signal(str)

    def __init__(self, dialog, parent=None):
        super().__init__(parent)
        self._dialog = dialog
        self._dialog.send_text.connect(self._emit_send_text)

    @Slot(str)
    def _emit_send_text(self, text):
        self.sendText.emit(text)

    @Slot(str)
    def receiveText(self, text):
        self._dialog.display_message(f"Received message: {text}")
