
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from .PlistEditTreeWidget import PlistEditTreeWidget

from PlistParser.Plist import PlistItem
from PlistParser.PlistParser import PlistParser


class PlistChoose(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(289, 284)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.label_3.setText(_translate("Form", "选择名称映射表"))
        self.label_2.setText(_translate("Form", "选择属性映射表"))
        self.label.setText(_translate("Form", "选择主数据文件"))

    def _1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*)")

class PyPlistEdit(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 337)
        Form.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top_widget = QtWidgets.QWidget(parent=Form)
        self.top_widget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.top_options = QtWidgets.QPushButton(parent=self.top_widget)
        self.top_options.setMinimumSize(QtCore.QSize(35, 34))
        self.top_options.setMaximumSize(QtCore.QSize(35, 34))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.top_options.setFont(font)
        self.top_options.setStyleSheet("")
        self.top_options.setObjectName("top_options")
        self.horizontalLayout.addWidget(self.top_options)
        self.top_body_widget = QtWidgets.QWidget(parent=self.top_widget)
        self.top_body_widget.setObjectName("top_body_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.top_body_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(parent=self.top_body_widget)
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.title_label.setFont(font)
        self.title_label.setToolTipDuration(-1)
        self.title_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.title_label.setLineWidth(0)
        self.title_label.setMidLineWidth(0)
        self.title_label.setIndent(0)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.info_label = QtWidgets.QLabel(parent=self.top_body_widget)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_2.addWidget(self.info_label)
        self.horizontalLayout.addWidget(self.top_body_widget)
        self.verticalLayout_3.addWidget(self.top_widget)
        self.body_horizontal_layout = QtWidgets.QHBoxLayout()
        self.body_horizontal_layout.setContentsMargins(-1, -1, 0, 0)
        self.body_horizontal_layout.setSpacing(0)
        self.body_horizontal_layout.setObjectName("body_horizontal_layout")
        self.option_widget = QtWidgets.QWidget(parent=Form)
        self.option_widget.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.option_widget.setObjectName("option_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.option_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.option_1 = QtWidgets.QPushButton(parent=self.option_widget)
        self.option_1.setObjectName("option_1")
        self.verticalLayout.addWidget(self.option_1)
        self.option_3 = QtWidgets.QPushButton(parent=self.option_widget)
        self.option_3.setObjectName("option_3")
        self.verticalLayout.addWidget(self.option_3)
        self.option_2 = QtWidgets.QPushButton(parent=self.option_widget)
        self.option_2.setObjectName("option_2")
        self.verticalLayout.addWidget(self.option_2)
        self.option_4 = QtWidgets.QPushButton(parent=self.option_widget)
        self.option_4.setObjectName("option_4")
        self.verticalLayout.addWidget(self.option_4)
        self.option_5 = QtWidgets.QPushButton(parent=self.option_widget)
        self.option_5.setObjectName("option_5")
        self.verticalLayout.addWidget(self.option_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.body_horizontal_layout.addWidget(self.option_widget)
        self.view_widget = QtWidgets.QWidget(parent=Form)
        self.view_widget.setMinimumSize(QtCore.QSize(30, 30))
        self.view_widget.setStyleSheet("background-color: rgb(64, 129, 193);")
        self.view_widget.setObjectName("view_widget")
        self.body_horizontal_layout.addWidget(self.view_widget)
        self.body_horizontal_layout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.body_horizontal_layout)
        self.bottom_info_label = QtWidgets.QLabel(parent=Form)
        self.bottom_info_label.setObjectName("bottom_info_label")
        self.verticalLayout_3.addWidget(self.bottom_info_label)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.view_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plist_edit_tree_widget = PlistEditTreeWidget()
        self.verticalLayout_4.addWidget(self.plist_edit_tree_widget)

        self.retranslateUi(Form)
        # self.info_label.hide()
        self.option_widget.hide()
        self.top_options.clicked.connect(lambda : self.option_widget.show() if self.option_widget.isHidden() else self.option_widget.hide())  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.top_options.setText(_translate("Form", "选项"))
        self.title_label.setText(_translate("Form",
                                            "<html><head/><body><p align=\"center\"><span style=\" color:#af7500;\">PyPlistEdit</span></p></body></html>"))
        self.info_label.setText(_translate("Form",
                                           "<html><head/><body><p align=\"right\"><span style=\" color:#ff0000;\">本程序尚且不完善 如存在一定问题(BUG)为正常现象非常抱歉 </span><a href=\"https://github.com/whiteEelsYikes/PlistParser\"><span style=\" text-decoration: underline; color:#0000ff; vertical-align:sub;\">项目链接</span></a><span style=\" color:#ff0000;\"> &lt;&lt;&lt; </span></p></body></html>"))
        self.option_1.setText(_translate("Form", "读取plist文件"))
        self.option_3.setText(_translate("Form", "写入plist文件"))
        self.option_2.setText(_translate("Form", "3"))
        self.option_4.setText(_translate("Form", "4"))
        self.option_5.setText(_translate("Form", "5"))
        self.bottom_info_label.setText(_translate("Form",
                                                  "<html><head/><body><p align=\"right\"><span style=\" color:#ff0000;\">2023/8/4--测试版 </span></p></body></html>"))

    def __raed_plist(self, path, map_dict, name_map_dict):
        pp = PlistParser()
        pp.parser_dict(path)
        plist = PlistItem((), None)
        plist.load_parse_dict(pp.plist_dict, map_dict)
        plist_dict = -plist
        plist_map_dict = plist.attribute_mapping_dict()
        plist_dict = plist.dict_key_replacement(plist_dict, plist_map_dict, True)
        plist_dict = plist.dict_key_replacement(plist_dict, name_map_dict, True)
        return plist_dict

    def __write_plist(self, py, plist_dict, map_dict, name_map_dict):
        plist = PlistItem((), None)
        name_map_dict = plist.attribute_mapping_dict_reverse(name_map_dict)
        plist_dict = plist.dict_key_replacement(plist_dict, name_map_dict, True)
        map_dict_ = plist.attribute_mapping_dict_reverse(map_dict)
        plist_dict = plist.dict_key_replacement(plist_dict, map_dict_, True)
        plist = type(f'Plist', (PlistItem,), {})
        plist = plist((), None)
        plist.load_parse_dict(plist_dict, map_dict)
        plist * py

    def raed_plist(self):
        pass

    def write_plist(self):
        pass




