from PyQt6 import QtWidgets
from DOMINIO.claseBodega import Bodega
from UI.pyUI.GestionBodega import  Ui_Dialog


class Bod(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.Bod = Bodega()
        self.ui.setupUi(self)
        self.inicializarControles()

        self.ui.btnAgregarBod.clicked.connect(self.btnAñadirBodega)

    def btnAñadirBodega(self):
        self.Bod.nombreBodega=self.ui.txtNombreBod.getText()
        self.Bod.tipobodega=self.ui.txtTipoBod.getText()
        self.Bod.ubicacion=self.ui.txtUbicacion.getText()
        self.Bod.descripcion=self.ui.lineEdit_4.getText()
        