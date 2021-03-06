# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basket_page_win.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QWidget)
import search

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #DAE5D0;\n"
"}")
        self.basket_shop_name = QLabel(Dialog)
        self.basket_shop_name.setObjectName(u"basket_shop_name")
        self.basket_shop_name.setGeometry(QRect(80, 20, 211, 41))
        font = QFont()
        font.setPointSize(30)
        self.basket_shop_name.setFont(font)
        self.basket_shop_name.setAlignment(Qt.AlignCenter)
        self.placeOrderButton = QPushButton(Dialog)
        self.placeOrderButton.setObjectName(u"placeOrderButton")
        self.placeOrderButton.setGeometry(QRect(10, 670, 351, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.placeOrderButton.setFont(font1)
        self.placeOrderButton.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(57, 68, 84);\n"
"	color: white;\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(111, 218, 156);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 4px solid green;\n"
"	background-color: rgb(80, 110, 125);\n"
"}")
        self.basket_shop_km = QLabel(Dialog)
        self.basket_shop_km.setObjectName(u"basket_shop_km")
        self.basket_shop_km.setGeometry(QRect(100, 60, 71, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.basket_shop_km.setFont(font2)
        self.basket_shop_mins = QLabel(Dialog)
        self.basket_shop_mins.setObjectName(u"basket_shop_mins")
        self.basket_shop_mins.setGeometry(QRect(190, 60, 91, 31))
        self.basket_shop_mins.setFont(font2)
        self.fixDeliveryToText = QLabel(Dialog)
        self.fixDeliveryToText.setObjectName(u"fixDeliveryToText")
        self.fixDeliveryToText.setGeometry(QRect(20, 90, 111, 31))
        font3 = QFont()
        font3.setPointSize(16)
        self.fixDeliveryToText.setFont(font3)
        self.addressLineEdit = QLineEdit(Dialog)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        self.addressLineEdit.setGeometry(QRect(10, 130, 351, 31))
        self.addressLineEdit.setFont(font3)
        self.addressLineEdit.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 1px solid black;\n"
"}")
        self.fixMyOrderText = QLabel(Dialog)
        self.fixMyOrderText.setObjectName(u"fixMyOrderText")
        self.fixMyOrderText.setGeometry(QRect(20, 170, 191, 31))
        self.fixMyOrderText.setFont(font3)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 200, 351, 331))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #DAE5D0;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}")
        self.basketScrollArea = QScrollArea(self.widget)
        self.basketScrollArea.setObjectName(u"basketScrollArea")
        self.basketScrollArea.setGeometry(QRect(0, 0, 351, 331))
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(16)
        self.basketScrollArea.setFont(font4)
        self.basketScrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: 6px inset #14C38E\n"
"}\n"
"")
        self.basketScrollArea.setWidgetResizable(True)
        self.basketScrollAreaWidgetContents = QWidget()
        self.basketScrollAreaWidgetContents.setObjectName(u"basketScrollAreaWidgetContents")
        self.basketScrollAreaWidgetContents.setGeometry(QRect(0, 0, 339, 319))
        self.basketScrollArea.setWidget(self.basketScrollAreaWidgetContents)
        self.fixFoodText = QLabel(Dialog)
        self.fixFoodText.setObjectName(u"fixFoodText")
        self.fixFoodText.setGeometry(QRect(20, 540, 191, 21))
        self.fixFoodText.setFont(font3)
        self.fixDeliveryFeeText = QLabel(Dialog)
        self.fixDeliveryFeeText.setObjectName(u"fixDeliveryFeeText")
        self.fixDeliveryFeeText.setGeometry(QRect(20, 570, 191, 21))
        self.fixDeliveryFeeText.setFont(font3)
        self.fixTotalText = QLabel(Dialog)
        self.fixTotalText.setObjectName(u"fixTotalText")
        self.fixTotalText.setGeometry(QRect(20, 600, 191, 21))
        self.fixTotalText.setFont(font3)
        self.all_food_price_label = QLabel(Dialog)
        self.all_food_price_label.setObjectName(u"all_food_price_label")
        self.all_food_price_label.setGeometry(QRect(260, 540, 91, 21))
        self.all_food_price_label.setFont(font3)
        self.all_food_price_label.setLayoutDirection(Qt.LeftToRight)
        self.all_food_price_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.delivery_fee_label = QLabel(Dialog)
        self.delivery_fee_label.setObjectName(u"delivery_fee_label")
        self.delivery_fee_label.setGeometry(QRect(260, 570, 91, 21))
        self.delivery_fee_label.setFont(font3)
        self.delivery_fee_label.setLayoutDirection(Qt.LeftToRight)
        self.delivery_fee_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.total_price_label = QLabel(Dialog)
        self.total_price_label.setObjectName(u"total_price_label")
        self.total_price_label.setGeometry(QRect(260, 600, 91, 21))
        self.total_price_label.setFont(font3)
        self.total_price_label.setLayoutDirection(Qt.LeftToRight)
        self.total_price_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.basketBackButton = QPushButton(Dialog)
        self.basketBackButton.setObjectName(u"basketBackButton")
        self.basketBackButton.setGeometry(QRect(20, 20, 41, 41))
        self.basketBackButton.setFont(font3)
        self.basketBackButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/searchicon/icons8-left-arrow-26.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(111, 218, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid black;\n"
"	background-color: rgb(140, 238, 179)\n"
"}")
        self.fixPaymentMethodText = QLabel(Dialog)
        self.fixPaymentMethodText.setObjectName(u"fixPaymentMethodText")
        self.fixPaymentMethodText.setGeometry(QRect(20, 630, 191, 21))
        self.fixPaymentMethodText.setFont(font3)
        self.paymentMethodComboBox = QComboBox(Dialog)
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.setObjectName(u"paymentMethodComboBox")
        self.paymentMethodComboBox.setGeometry(QRect(200, 630, 151, 25))
        self.paymentMethodComboBox.setFont(font3)
        self.paymentMethodComboBox.setLayoutDirection(Qt.LeftToRight)
        self.paymentMethodComboBox.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/searchicon/icons8-expand-arrow-24.png);\n"
"	margin-right: 6px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 3px solid #00FFAB\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	border: 1px soild rgba(0,0,0,10%);\n"
"	background-color: #fff;\n"
"	outline: 0px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover{\n"
"	background-color: rgba(184,241,176, 50%);\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.basket_shop_name.setText(QCoreApplication.translate("Dialog", u"Shop name", None))
        self.placeOrderButton.setText(QCoreApplication.translate("Dialog", u"Place Order", None))
        self.basket_shop_km.setText(QCoreApplication.translate("Dialog", u"10 km", None))
        self.basket_shop_mins.setText(QCoreApplication.translate("Dialog", u"50 mins", None))
        self.fixDeliveryToText.setText(QCoreApplication.translate("Dialog", u"Delivery to", None))
        self.addressLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u" Address", None))
        self.fixMyOrderText.setText(QCoreApplication.translate("Dialog", u"My Order", None))
        self.fixFoodText.setText(QCoreApplication.translate("Dialog", u"Food", None))
        self.fixDeliveryFeeText.setText(QCoreApplication.translate("Dialog", u"Delivery fee", None))
        self.fixTotalText.setText(QCoreApplication.translate("Dialog", u"Total", None))
        self.all_food_price_label.setText(QCoreApplication.translate("Dialog", u"\u0e3f1000", None))
        self.delivery_fee_label.setText(QCoreApplication.translate("Dialog", u"\u0e3f1000", None))
        self.total_price_label.setText(QCoreApplication.translate("Dialog", u"\u0e3f1000", None))
        self.basketBackButton.setText("")
        self.fixPaymentMethodText.setText(QCoreApplication.translate("Dialog", u"Payment method", None))
        self.paymentMethodComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Cash", None))
        self.paymentMethodComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Rabbit Line Pay", None))
        self.paymentMethodComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"K PLUS", None))
        self.paymentMethodComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"SCB EASY", None))

    # retranslateUi

