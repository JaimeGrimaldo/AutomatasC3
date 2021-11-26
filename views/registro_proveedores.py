# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_proveedores.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VentanaRegistroProveedores(object):
    def setupUi(self, VentanaRegistroProveedores):
        if not VentanaRegistroProveedores.objectName():
            VentanaRegistroProveedores.setObjectName(u"VentanaRegistroProveedores")
        VentanaRegistroProveedores.resize(400, 267)
        VentanaRegistroProveedores.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(VentanaRegistroProveedores)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 221, 21))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label_2 = QLabel(VentanaRegistroProveedores)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 111, 21))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        self.label_2.setFont(font1)
        self.Field_nombreProveedor = QLineEdit(VentanaRegistroProveedores)
        self.Field_nombreProveedor.setObjectName(u"Field_nombreProveedor")
        self.Field_nombreProveedor.setGeometry(QRect(170, 70, 151, 20))
        self.label_3 = QLabel(VentanaRegistroProveedores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 110, 71, 21))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.label_3.setFont(font2)
        self.Field_nombreProducto = QLineEdit(VentanaRegistroProveedores)
        self.Field_nombreProducto.setObjectName(u"Field_nombreProducto")
        self.Field_nombreProducto.setGeometry(QRect(150, 110, 171, 20))
        self.label_4 = QLabel(VentanaRegistroProveedores)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 150, 71, 21))
        self.label_4.setFont(font2)
        self.field_codigoProveedor = QLineEdit(VentanaRegistroProveedores)
        self.field_codigoProveedor.setObjectName(u"field_codigoProveedor")
        self.field_codigoProveedor.setGeometry(QRect(150, 150, 171, 20))
        self.Boton_confirmarRegistro = QPushButton(VentanaRegistroProveedores)
        self.Boton_confirmarRegistro.setObjectName(u"Boton_confirmarRegistro")
        self.Boton_confirmarRegistro.setGeometry(QRect(140, 200, 131, 51))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        self.Boton_confirmarRegistro.setFont(font3)
        self.Boton_confirmarRegistro.setCursor(QCursor(Qt.OpenHandCursor))

        self.retranslateUi(VentanaRegistroProveedores)

        QMetaObject.connectSlotsByName(VentanaRegistroProveedores)
    # setupUi

    def retranslateUi(self, VentanaRegistroProveedores):
        VentanaRegistroProveedores.setWindowTitle(QCoreApplication.translate("VentanaRegistroProveedores", u"Registrar proveedores", None))
        self.label.setText(QCoreApplication.translate("VentanaRegistroProveedores", u"Registro de proveedores", None))
        self.label_2.setText(QCoreApplication.translate("VentanaRegistroProveedores", u"Nombre (contacto):", None))
        self.label_3.setText(QCoreApplication.translate("VentanaRegistroProveedores", u"Producto:", None))
        self.label_4.setText(QCoreApplication.translate("VentanaRegistroProveedores", u"C\u00f3digo", None))
        self.Boton_confirmarRegistro.setText(QCoreApplication.translate("VentanaRegistroProveedores", u"CONFIRMAR", None))
    # retranslateUi

