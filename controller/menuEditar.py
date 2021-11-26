from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from PySide2.QtCore import Qt
from views.menu_editar import MenuEditar

class MenuEdit(QWidget,MenuEditar):
      def __init__(self, parent = None) -> None:
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowFlag(Qt.Window)
            self.BotonActivar.clicked.connect(self.EditUsuario)
            self.BotonActivar_3.clicked.connect(self.EditProveedor)
            
      def EditUsuario(self):
            from controller.ListUser import ListadoUsuarios
            window = ListadoUsuarios(self)
            window.show()
      
      
      def EditProveedor(self):
            from controller.listaProveedores import ListadoProveedores
            window = ListadoProveedores(self)
            window.show()
      
      
          