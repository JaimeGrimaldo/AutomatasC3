# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_proveedores.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ventana_listaProveedores(object):
    def setupUi(self, Ventana_listaProveedores):
        if not Ventana_listaProveedores.objectName():
            Ventana_listaProveedores.setObjectName(u"Ventana_listaProveedores")
        Ventana_listaProveedores.resize(634, 352)
        self.label = QLabel(Ventana_listaProveedores)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 271, 31))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(16)
        self.label.setFont(font)
        self.table_proveedores = QTableWidget(Ventana_listaProveedores)
        self.table_proveedores.setObjectName(u"table_proveedores")
        self.table_proveedores.setGeometry(QRect(30, 70, 571, 192))
        self.boton_Editar = QPushButton(Ventana_listaProveedores)
        self.boton_Editar.setObjectName(u"boton_Editar")
        self.boton_Editar.setGeometry(QRect(250, 280, 151, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.boton_Editar.setFont(font1)

        self.retranslateUi(Ventana_listaProveedores)

        QMetaObject.connectSlotsByName(Ventana_listaProveedores)
    # setupUi

    def retranslateUi(self, Ventana_listaProveedores):
        Ventana_listaProveedores.setWindowTitle(QCoreApplication.translate("Ventana_listaProveedores", u"Lista de proveedores para su edici\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Ventana_listaProveedores", u"SELECCIONAR PROVEEDOR", None))
        self.boton_Editar.setText(QCoreApplication.translate("Ventana_listaProveedores", u"EDITAR PROVEEDOR", None))
    # retranslateUi

