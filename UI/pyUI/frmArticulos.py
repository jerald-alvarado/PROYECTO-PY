# Form implementation generated from reading ui file 'frmArticulos.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 358)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.txtArticulo = QtWidgets.QLineEdit(parent=Dialog)
        self.txtArticulo.setGeometry(QtCore.QRect(130, 20, 151, 20))
        self.txtArticulo.setObjectName("txtArticulo")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(520, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txtBuscarArtc = QtWidgets.QLineEdit(parent=Dialog)
        self.txtBuscarArtc.setGeometry(QtCore.QRect(570, 20, 151, 20))
        self.txtBuscarArtc.setObjectName("txtBuscarArtc")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.txtDescripcionArti = QtWidgets.QTextEdit(parent=Dialog)
        self.txtDescripcionArti.setGeometry(QtCore.QRect(40, 100, 521, 151))
        self.txtDescripcionArti.setObjectName("txtDescripcionArti")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label_4.setObjectName("label_4")
        self.txtCantidadArtic = QtWidgets.QLineEdit(parent=Dialog)
        self.txtCantidadArtic.setGeometry(QtCore.QRect(360, 20, 81, 20))
        self.txtCantidadArtic.setObjectName("txtCantidadArtic")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 60, 47, 13))
        self.label_5.setObjectName("label_5")
        self.comboBoxBodegasExistentes = QtWidgets.QComboBox(parent=Dialog)
        self.comboBoxBodegasExistentes.setGeometry(QtCore.QRect(570, 60, 151, 22))
        self.comboBoxBodegasExistentes.setAccessibleDescription("")
        self.comboBoxBodegasExistentes.setCurrentText("")
        self.comboBoxBodegasExistentes.setObjectName("comboBoxBodegasExistentes")
        self.btnAgregar = QtWidgets.QPushButton(parent=Dialog)
        self.btnAgregar.setGeometry(QtCore.QRect(90, 290, 75, 23))
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnActualizar = QtWidgets.QPushButton(parent=Dialog)
        self.btnActualizar.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnEliminar = QtWidgets.QPushButton(parent=Dialog)
        self.btnEliminar.setGeometry(QtCore.QRect(460, 290, 75, 23))
        self.btnEliminar.setObjectName("btnEliminar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nombre del artículo:"))
        self.label_2.setText(_translate("Dialog", "Buscar:"))
        self.label_3.setText(_translate("Dialog", "Descripción:"))
        self.label_4.setText(_translate("Dialog", "Cantidad:"))
        self.label_5.setText(_translate("Dialog", "Bodegas:"))
        self.btnAgregar.setText(_translate("Dialog", "Agregar"))
        self.btnActualizar.setText(_translate("Dialog", "Actualizar"))
        self.btnEliminar.setText(_translate("Dialog", "Eliminar"))