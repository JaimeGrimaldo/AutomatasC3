from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox,QAbstractItemView
from PySide2.QtCore import Qt
from views.lista_proveedores import Ventana_listaProveedores
from db.PuntoVenta import ListProveedor

class ListadoProveedores(QWidget, Ventana_listaProveedores):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.boton_Editar.clicked.connect(self.abrirProv)
        self.tableConfig()
        self.listar(ListProveedor())
    
    def abrirProv(self):
        from controller.editarProveedores import EditarProveedoress
        selecRow = self.table_proveedores.selectedItems()
        if selecRow:
            idU = str(selecRow[0].text())
            window = EditarProveedoress(self,idU)
            window.show()
        self.table_proveedores.clearSelection()

    def tableConfig(self):
        columHeader = ("ID","Nombre","Producto","Codigo")
        self.table_proveedores.setColumnCount(len(columHeader))
        self.table_proveedores.setHorizontalHeaderLabels(columHeader)
        self.table_proveedores.setSelectionBehavior(QAbstractItemView.SelectRows)

    def listar(self,data):
        self.table_proveedores.setRowCount(len(data))
        for(indexRow,row) in enumerate(data):
            for(indexCell,cell) in enumerate(row):
                self.table_proveedores.setItem(indexRow,indexCell,QTableWidgetItem(str(cell)))

    


