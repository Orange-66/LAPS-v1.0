# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/ui_caution.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Caution(object):
    def setupUi(self, Caution):
        Caution.setObjectName("Caution")
        Caution.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Caution)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Caution)
        self.buttonBox.accepted.connect(Caution.accept)
        self.buttonBox.rejected.connect(Caution.reject)
        QtCore.QMetaObject.connectSlotsByName(Caution)

    def retranslateUi(self, Caution):
        _translate = QtCore.QCoreApplication.translate
        Caution.setWindowTitle(_translate("Caution", "注意"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Caution = QtWidgets.QDialog()
    ui = Ui_Caution()
    ui.setupUi(Caution)
    Caution.show()
    sys.exit(app.exec_())
