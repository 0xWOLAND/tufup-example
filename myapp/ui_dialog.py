# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.input = QLineEdit(Dialog)
        self.input.setObjectName("input")

        self.gridLayout.addWidget(self.input, 1, 0, 1, 1)

        self.send = QPushButton(Dialog)
        self.send.setObjectName("send")

        self.gridLayout.addWidget(self.send, 1, 1, 1, 1)

        self.output = QPlainTextEdit(Dialog)
        self.output.setObjectName("output")
        self.output.setReadOnly(True)
        self.output.setPlainText("Initializing WebChannel...")
        self.output.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.output, 0, 0, 1, 2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.input.setPlaceholderText(
            QCoreApplication.translate("Dialog", "Message Contents", None)
        )
        self.send.setText(QCoreApplication.translate("Dialog", "Send", None))

    # retranslateUi
