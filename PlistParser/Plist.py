#!/usr/bin/python3
# -*- coding: utf-8 -*-


class PlistItem:
    """
    记住 PlistItem 实现 默认没有对 class属性的支持 仅对 self属性支持
    这里 默认请使用self来绑定对应属性 而不是使用class 因为 PlistItem的算法目前 对self绑定注册的属性支持和保障是最好的
    """

    def __init__(self, item_index_tuple, item, data=None, name=None, item_index_head=''):
        """

        :param item_index_tuple:
        :param item: 当前节点在 .plist 中的名称 (key值)
        :param data: 当前节点的数据
        :param name: 当前节点在 PlistItem 中的属性名 str字符
        :param item_index_head: 当前节点的 前缀头数据 在  __pos__ __neg__ __invert__ 中引用拼接 节点路径前缀
        """
        self.name = name
        self.item_index_tuple = item_index_tuple
        self.item = item
        self.item_index_head = item_index_head
        self.data = data
        self.dict = None
        self.dict_index = None
        self.path = None
        self.path_tuple = None
        self.update()

    def update(self, item_index_tuple=None, item=None, data=None, name=None, item_index_head=None):
        """
        更新实例属性 也相当于更新节点属性 会更改self数据
        :param item_index_tuple:
        :param item: 当前节点在 .plist 中的名称 (key值)
        :param data: 当前节点的数据
        :param item_index_head: 当前节点的 前缀头数据 在  __pos__ __neg__ __invert__ 中引用拼接 节点路径前缀
        :return:
        """
        item_index_tuple = self.item_index_tuple if item_index_tuple == None else item_index_tuple
        item = self.item if item == None else item
        data = self.data if data == None else data
        name = self.name if name == None else name
        item_index_head = self.item_index_head if item_index_head == None else item_index_head

        dict_index = None
        path = None
        dict_ = {}
        index_ = dict_
        tuple_item = item_index_tuple + (item,)
        tuple_item_last = len(tuple_item) - 1
        for item_ in tuple_item:
            dict_index = f'{dict_index}["{item_}"]' if dict_index != None else f'["{item_}"]'
            path = f'{path}.{item_}' if path != None else f'{item_}'
            index_[item_] = {} if tuple_item.index(item_) < tuple_item_last else data
            index_ = index_[item_]
        dict_index, path, path_tuple = (
            f'{item_index_head}{dict_index}',
            f'{item_index_head}.{path}',
            item_index_tuple + (item,)
        ) if item_index_head else (
            dict_index,
            path,
            item_index_tuple + (item,)
        )

        self.item_index_tuple = item_index_tuple
        self.item = item
        self.item_index_head = item_index_head
        self.data = data
        self.name = name
        self.dict = dict_
        self.dict_index = dict_index
        self.path = path
        self.path_tuple = path_tuple
        return (self.item_index_tuple,
                self.item,
                self.item_index_head,
                self.dict_index,
                self.path,
                self.path_tuple,
                )

    def simplification_dict(self, plist_dict=None):
        """
        将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict
        与 PlistParser.PlistParser.plist_dict 相同
        :param plist_dict: 指定该参数则会将解析的 dict 数据更新在指定的 plist_dict 中
        :return: 完成解析的 dict

        """
        plist_dict = {} if plist_dict == None else plist_dict
        for self_item, self_item_value in self.__dict__.items():
            if isinstance(self_item_value, PlistItem):
                item = self_item_value.item
                index_tuple = self_item_value.item_index_tuple
                data = self_item_value.data
                item_item = {} if item in index_tuple else data
                plist_dict[item] = item_item
                if type(item_item) == dict:
                    self_item_value.simplification_dict(item_item)
        return plist_dict

    def dict_key_replacement(self, replacement_dict, mapping_dict, key_error=None):
        """
        在 mapping_dict 中查找 replacement_dict 对应的 key 的替换值 并将其替换

        :param replacement_dict: key 被替换的 dict
        :param mapping_dict:  替换 key 的映射 dict
        :param key_error:  当出现 mapping_dict 找不到 replacement_dict 中对应的key 时 是否自动跳过
        :return:

        replacement_dict 与 mapping_dict 的关系:
            ...
        """
        map_dict = {}
        for key, value in replacement_dict.items():
            if type(value) == dict:
                try:
                    mapping_dict_dict = mapping_dict[key]
                    map_dict_key = mapping_dict_dict[key]
                except KeyError:
                    if key_error:
                        continue
                    raise
                map_dict[map_dict_key] = self.dict_key_replacement(value, mapping_dict_dict, key_error)
            else:
                try:
                    map_dict_key = mapping_dict[key]
                except KeyError:
                    if key_error:
                        continue
                    raise
                map_dict[map_dict_key] = value
        return map_dict

    def attribute_mapping_dict(self, attribute_mapping_dict=None):
        """
        分析并返回当前节点以及下级节点的 attribute_mapping_dict
        :param attribute_mapping_dict: 上级 attribute_mapping_dict 默认情况下为回调使用 默认参数即可
        :return:

        返回的 dict 为: ( 相当于 标准 attribute_mapping_dict )
                    {
                        'a': 'a name',
                        'b': 'b name',
                        'c': {
                            'c' : 'c name'  # 这里重复以下 这个'c' key的名字映射 因为c是一个字典所有只能用在字典里重复'c'key的方法兼容映射其对应的属性(节点)名称
                            'd' : 'a name',
                            'e' : 'e name',
                        },
                    }
        """
        attribute_mapping_dict = {} if attribute_mapping_dict == None else attribute_mapping_dict
        for self_item, self_item_value in self.__dict__.items():
            if isinstance(self_item_value, PlistItem):
                item_ = self_item_value.item
                index_tuple = self_item_value.item_index_tuple
                item_item = {f'{item_}': self_item} if item_ in index_tuple else self_item
                attribute_mapping_dict[item_] = item_item
                if type(item_item) == dict:
                    self_item_value.attribute_mapping_dict(item_item)
        return attribute_mapping_dict

    def attribute_mapping_dict_reverse(self, attribute_mapping_dict):
        """
        颠倒 attribute_mapping_dict_reverse 的 key 和 value
        :param attribute_mapping_dict: 被颠倒 key value 的 attribute_mapping_dict
        :return:

        attribute_mapping_dict 应为:
                    {
                        'a': 'a name',
                        'b': 'b name',
                        'c': {
                            'c' : 'c name'  # 这里重复以下 这个'c' key的名字映射 因为c是一个字典所有只能用在字典里重复'c'key的方法兼容映射其对应的属性(节点)名称
                            'd' : 'a name',
                            'e' : 'e name',
                        },
                    }
        """
        map_dict = {}
        for key, value in attribute_mapping_dict.items():
            if type(value) == dict:
                key = value[key]
                map_dict[key] = self.attribute_mapping_dict_reverse(value)
            else:
                map_dict[value] = key
        return map_dict

    def load_parse_dict(self, load_dict, attribute_mapping_dict, index_tuple=None, class_item_obj=None, key_error=None):
        """
        提供将 parse_dict  插入 并更新到 此节点 会直接改变 self的数据
        :param load_dict:  需要插入当前节点的 parse_dict
        :param attribute_mapping_dict:  属性映射表
        :param index_tuple:  路径 以元组为表达方式 一般情况可以不管这个参数 是方法回调递归时自动处理的
        :param key_error:  当出现 attribute_mapping_dict 找不到 load_dict 中对应的key 时 是否自动跳过
        :return: 当前节点 self

        load_dict 与 attribute_mapping_dict 详解:
            这两个都是字典
            PlistItem.load_parse_dict扫描load_dict时 需要依赖attribute_mapping_dict来构建属性(节点) 确认属性(节点)名称这些
            load_dict 与 attribute_mapping_dict 是相互关联的
            attribute_mapping_dict中记录的是load_dict每个key的名字
            例如:
                load_dict 为以下时 则:
                    {
                        'a': 1,
                        'b': 2,
                        'c': {
                            'd' : 2,
                            'e' : 'str',
                        },
                    }
                attribute_mapping_dict 应为:
                    {
                        'a': 'a name',
                        'b': 'b name',
                        'c': {
                            'c' : 'c name'  # 这里重复以下 这个'c' key的名字映射 因为c是一个字典所有只能用在字典里重复'c'key的方法兼容映射其对应的属性(节点)名称
                            'd' : 'a name',
                            'e' : 'e name',
                        },
                    }
                如果 load_dict 中有(任何)一个key 没有存在 attribute_mapping_dict 中登记对应名字时:
                    我们想要跳过这个没有在 attribute_mapping_dict 中进行登记的 load_dict的key 就可以使用:
                        PlistItem.load_parse_dict 的 key_error 参数
                        注意当 attribute_mapping_dict 没有存在 load_dict 中的任何一个key时:
                            如果没有使用 PlistItem.load_parse_dict 的 key_error 参数 都会直接触发报错 (尽管可以修改源代码得到其他目的)

        """
        index_tuple = () if index_tuple == None else index_tuple
        for key, value in load_dict.items():
            index_tuple_ = index_tuple
            mapping_dict_key = attribute_mapping_dict.get(key)
            if mapping_dict_key == None:
                if key_error:
                    continue
                raise KeyError(f'attribute_mapping_dict 中没有找到 {key} 的 dict key')
            mapping_dict_key_ = mapping_dict_key
            if type(mapping_dict_key) == dict:
                mapping_dict_key_ = mapping_dict_key.get(key)
                if mapping_dict_key_ == None:
                    if key_error:
                        continue
                    raise KeyError(f'attribute_mapping_dict{index_tuple_} 的 dict key')
            if type(value) == dict:
                index_tuple_ += (key,)
                key_class = type(f'{mapping_dict_key_}', (PlistItem,), {})
                class_item_obj_ = type(f'{mapping_dict_key_}Item', (PlistItem,), {})
                key_class = key_class(index_tuple_, key, value, value, mapping_dict_key_).load_parse_dict(value,
                                                                                                          mapping_dict_key,
                                                                                                          index_tuple_,
                                                                                                          class_item_obj_,
                                                                                                          key_error)
            else:
                key_class = PlistItem if class_item_obj == None else class_item_obj
                key_class = key_class(index_tuple_, key, value, mapping_dict_key_)
            self.__dict__[mapping_dict_key_] = key_class
        return self

    def save_py_file(self, type_index=None):
        """
        将当前节点及以下节点 转换为 标准的 .py文件 提供永久的py源码存储方式
        此方法无法直接保存文件 而是 会返回 符合 py语法的 字符数据
        该方法使用递归实现
        :param type_index: 默认调用时不用管这个参数 主要是留给 递归 验证 是否已经存在 一个 class 定义 防止 重复 定义
        :return:
        """
        py_head = '"""\n .Py Plist Data\n 本程序为.Plist的.py版本\n GitHub: https://github.com/whiteEelsYikes/PlistParser\n PyPi: https://pypi.org/project/PlistParser/\n 略...\n"""'
        py_import = '' if type_index else f'{py_head}\nfrom PlistParser.Plist import PlistItem\n\n\n'
        type_index = {} if type_index == None else type_index
        self_type = type(self)
        class_name = self_type.__name__
        class_parent = ['('] + [item.__name__ + ',' for item in self_type.__bases__ if item != object] + [')']
        class_parent = ''.join(class_parent)
        class_item = ''
        class_inner = ''
        class_str = ''
        self_item = self.__dict__
        if tuple(self_item.keys()) == tuple(PlistItem((), '').__dict__.keys()):
            if class_name != PlistItem.__name__ and not type_index.get(class_name):
                type_index[class_name] = True
                return f'class {class_name}{class_parent}:\n    pass\n\n'
            else:
                return class_str
        for key, value in self_item.items():
            if isinstance(value, PlistItem):
                value_class = type(value)
                obj_name = value_class.__name__
                index_tuple = value.item_index_tuple
                item = value.item
                data = value.data
                name = key
                head = value.item_index_head
                data_type = type(data)
                if data_type == str:
                    data = f"""'{data}'"""
                elif data_type == dict:
                    data = None
                class_item += f"        self.{key} = {obj_name}({index_tuple}, '{item}', {data}, '{name}', '{head}')\n"
                type_index[class_name] = True
                class_inner += value.save_py_file(type_index=type_index)
            else:
                pass
                class_item += f'        self.{key} = {value}\n' if type(
                    value) != str else f"        self.{key} = '{value}'\n"
        class_str = f"""\
class {class_name}{class_parent}:
    def __init__(self, item_index_tuple=None, item=None, data=None, name=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, data, name, item_index_head=item_index_head)
        \n{class_item}\n"""
        return py_import + class_inner + class_str

    def __pos__(self):
        """
        重载 单目运算符 +
        返回一个 可以用于字典取值的 str 路径
        :return:
        """
        return self.dict_index

    def __neg__(self):
        """
        重载 单目运算符 -
        返回 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict 数据
        :return:
        """
        return self.simplification_dict()

    def __invert__(self):
        """
        重载 单目运算符 ~
        返回 当前节点的路径 以 元组 表达的 节点路径
        :return:
        """
        return self.path_tuple

    def __add__(self, other):
        """
        重载 双目运算符 +
        提供 对目标 数据 进行  结合 将当前节点插入 找到的运算参数中 不会改动self数据
        :param other:
        :return:
        """
        other_type = type(other)
        if other_type == dict:
            return self.simplification_dict(other)
        elif other_type == list:
            return other + [self.simplification_dict(), ]
        elif other_type == tuple:
            return other + (self.simplification_dict(),)

    def __sub__(self, other):
        """
        重载 双目运算符 -
        提供 对目标 数据 进行 去除 将当前节点去除 找到的运算参数中  不会改动self数据
        :param other:
        :return:
        """
        other_type = type(other)
        dict_ = {}
        if other_type == dict:
            simplification_dict = self.simplification_dict().keys()
            for key, value in other.items():
                if key in simplification_dict:
                    continue
                dict_[key] = value
        return dict_

    def __mul__(self, other: str):
        """
        重载 双目运算符 *
        提供 保存当前 节点为 文件 格式为标准的 .py 文件
        :param other:
        :return:
        """
        with open(other, 'w', encoding='utf-8') as file:
            file.write(self.save_py_file())
        return None
