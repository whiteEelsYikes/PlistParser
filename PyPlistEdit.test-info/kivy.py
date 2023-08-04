
from kivy.app import App
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class PlistTreeViewLabelMenu(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PlistTreeViewLabel(TreeViewLabel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu = PlistTreeViewLabelMenu()

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            print('Mouse scrolling')
        elif touch.is_double_tap:  # 双击
            self.menu.open()
        elif touch.is_triple_tap:
            print('Triple tap')
        else:
            print('Other touch event')

class PlistTreeViewMenu(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Button(text='I have a dream!')

class PlistTreeView(TreeView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu = PlistTreeViewMenu(title='属性编辑器', content=Button(text='Popup Content'), size_hint=(None, None), size=(200, 200))

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            super().on_touch_down(touch)
        elif touch.is_double_tap:  # 双击
            self.menu.open()
        elif touch.is_triple_tap:
            super().on_touch_down(touch)
        else:
            super().on_touch_down(touch)

    def load_Plist_dict(self, plist_dict, parent=None):
        parent = self if parent == None else parent
        for key, value in plist_dict.items():
            child = QTreeWidgetItem(parent)
            child.setText(0, str(key))
            end = value
            value = value if isinstance(value, dict) else {value:None}
            if end != None:
                self.load_Plist_dict(value, child)




class TreeViewApp(App):
    def build(self):
        tree = PlistTreeView(root_options=dict(text='Languages'), hide_root=False)
        python = tree.add_node(PlistTreeViewLabel(text='Python'))
        java = tree.add_node(PlistTreeViewLabel(text='Java'))
        tree.add_node(PlistTreeViewLabel(text='C++'), java)
        tree.add_node(PlistTreeViewLabel(text='C#'), java)
        tree.add_node(PlistTreeViewLabel(text='Ruby'), python)
        print(list(tree.iterate_all_nodes()))
        return tree




if __name__ == '__main__':
    TreeViewApp().run()

