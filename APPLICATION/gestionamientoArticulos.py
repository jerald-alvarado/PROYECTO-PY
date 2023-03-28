from PyQt6 import QtWidgets
from DOMINIO.claseArticulos import Articulos
from UI.pyUI.frmArticulos import  Ui_Dialog


class Art(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.art = Articulos()
        self.inicializarControles()
        
        self.ui.btnAgregar.clicked.connect(self.btnAgregar_Art)
        self.ui.btnActualizar.clicked.connect(self.btnActualizar_Art)
        self.ui.btnEliminar.clicked.connect(self.btnEliminar_Art)
        
    def btnAgregar_Art(self):
        self.art.bodega = self.ui.comboBoxBodegasExistentes.currentIndex()
        self.art.nombre = self.ui.txtArticulo.getText()
        self.art.descripcion = self.ui.txtDescripcionArti.getText()
        self.art.cantidad = self.ui.txtCantidadArtic.getText()

    def btnActualizar_Art(self):
        self.art.bodegabodega = self.ui.comboBoxBodegasExistentes.curtrentIndex()
        self.art.descripcion = self.ui.txtDescripcionArti.getText()
        self.art.cantidad = self.ui.txtCantidadArtic.getText()

    def btnEliminar_Art(self):
        self.art.nombre = self.ui.txtArticulo.getText()



