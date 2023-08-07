

from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMenu,QInputDialog, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class PlistEditTreeWidget(QTreeWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.clipboard = QApplication.clipboard()
        self.setHeaderLabels(['PlistEditTreeWidget'])
        self.setHeaderHidden(True)
        self.setDragEnabled(True)

    def load_plist_dict(self, plist_dict, parent=None):
        parent = self if parent == None else parent
        for key, value in plist_dict.items():
            child = QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemFlag.ItemIsEditable)
            child.setText(0, str(key))
            end = value
            type_value = type(value)
            if type_value in [type, list]:
                value = str(value)
            value = value if isinstance(value, dict) else {value:None}
            if end != None:
                self.load_plist_dict(value, child)

    def export_plist_dict(self, item=None):
        result = {}
        if item == None:
            item = self.invisibleRootItem()
            item = item.child(0)
        for i in range(item.childCount()):
            child = item.child(i)
            if child.childCount() > 0:
                result[child.text(0)] = self.export_plist_dict(child)
            else:
                try:
                    return eval(child.text(0))
                except:
                    return child.text(0)
        return result

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        copy_value_action = QAction('复制值')
        copy_value_action.setShortcut('Ctrl+c')
        copy_value_action.triggered.connect(self.copy_selected_value)
        copy_dict_action = QAction('复制键值')
        copy_dict_action.setShortcut('Ctrl+Alt+c')
        copy_dict_action.triggered.connect(self.copy_selected_dict)
        copy_node_action = QAction('复制节点')
        copy_node_action.setShortcut('Ctrl+Shift+c')
        copy_node_action.triggered.connect(self.copy_selected_node)
        add_new_value = QAction('插入值')
        add_new_value.setShortcut('Ctrl+v')
        add_new_value.triggered.connect(self.add_new_value)
        add_new_dict = QAction('插入键值')
        add_new_dict.setShortcut('Ctrl+Alt+v')
        add_new_dict.triggered.connect(self.add_new_dict)
        add_new_node = QAction('插入节点')
        add_new_node.setShortcut('Ctrl+Shift+v')
        add_new_node.triggered.connect(self.add_new_node)
        delete_node_value = QAction(r'删除值\节点')
        delete_node_value.setShortcut('Ctrl+d')
        delete_node_value.triggered.connect(self.delete_node_value)
        menu.addAction(copy_value_action)
        menu.addAction(copy_dict_action)
        menu.addAction(copy_node_action)
        menu.addAction(add_new_value)
        menu.addAction(add_new_dict)
        menu.addAction(add_new_node)
        menu.addAction(delete_node_value)
        menu.exec(event.globalPos())

    def copy_selected_value(self):
        selected_item = self.selectedItems()[0]
        self.clipboard.setText(selected_item.text(0))

    def copy_selected_dict(self):
        selected_item = self.selectedItems()[0]
        selected_item_parent = selected_item.parent()
        selected_item_parent_text = None
        if selected_item_parent != None:
            selected_item_parent_text = selected_item_parent.text(0)
        selected_dict = {
            selected_item_parent_text:selected_item.text(0)
        }
        self.clipboard.setText(str(selected_dict))

    def copy_selected_node(self):
        selected_item = self.selectedItems()[0]
        selected_item_parent = selected_item.parent()
        if selected_item_parent != None:
            selected_item_parent_text = selected_item_parent.text(0)
        else:
            selected_item_parent_text = selected_item.text(0)
        selected_dict = {
            selected_item_parent_text: self.export_plist_dict(selected_item)
        }
        self.clipboard.setText(str(selected_dict))

    def add_new_value(self):
        selected_item = self.selectedItems()
        no_selected_item = False
        if not selected_item:
            no_selected_item = True
        else:
            selected_item = selected_item[0]
        text, ok = QInputDialog.getText(self, '新增值', '请输入值的文本:')
        if not ok:
            return
        if no_selected_item:
            child = QTreeWidgetItem(self)
            child.setFlags(child.flags() | Qt.ItemFlag.ItemIsEditable)
            child.setText(0, str(text))
        else:
            self.load_plist_dict({text:''}, selected_item)

    def add_new_dict(self):
        selected_item = self.selectedItems()[0]
        text, ok = QInputDialog.getText(self, '新增键值', '请输入键值的字典文本:')
        if ok:
            try:
                text = eval(text)
                if type(text) != dict:
                    raise ValueError('需要字典数据')
                self.load_plist_dict(text, selected_item)
            except Exception as error:
                QMessageBox.warning(self, '新增键值失败', f'信息:\n{error}')

    def add_new_node(self):
        selected_item = self.selectedItems()[0]
        text, ok = QInputDialog.getText(self, '新增节点', '请输入节点的字典文本:')
        if ok:
            try:
                text = eval(text)
                if type(text) != dict:
                    raise ValueError('需要字典数据')
                self.load_plist_dict(text, selected_item)
            except Exception as error:
                QMessageBox.warning(self, '新增节点失败', f'信息:\n{error}')

    def delete_node_value(self):
        item = self.selectedItems()[0]
        (item.parent() or self.invisibleRootItem()).removeChild(item)

