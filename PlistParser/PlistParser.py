#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import plistlib


class PlistParser:

    def __init__(self, parser_plist: str | dict | None = None, auto_parser: bool = True, cust_dict: dict = None):
        """

        :param parser_plist: 给定解析的 .plist 文件 或者 二进制 或者 文本 数据
        :param auto_parser: 是否在 plist_txt 不为空时 自动在初始化时解析 plist_txt (在 plist_txt 为空时 该参数不会有任何效果)
        :param cust_dict: 全称 customization_dict 给定自定义的 plist 字典数据
        """
        if type(parser_plist) == dict:
            self.__dict__ = parser_plist
            return
        self.plist_data = parser_plist
        self.plist_dict = self.parser_dict(parser_plist) if auto_parser and parser_plist != None else None
        self.cust_dict = cust_dict

    def parser_base64(self, bytes_data: bytes | str, mode_dict: dict) -> bytes | str:  # base 16 32 64 加解密支持
        """
        提供强大的 base64 基础加解密支持 可支持嵌套加解密
        :param bytes_data: 被这些操作的(加解密)数据
        :param mode_dict: 加解密操作及其参数声明字典
        :return: 执行 mode_dict 指定操作后的 加解密 数据
                    (一开始传入的bytes_data是什么类型就返回什么类型)

        mode_dict 详解:
            {
            base64加解密函数 : 参数字典,
            base64.b64encode:{},  # 先执行 加密操作
            Base64.Decode.bit64:{},  # 在执行一次 解密操作
            Base64.Encode.bit32:{},  # 在执行一次 32bit的加密操作
            }

        """
        bytes_data_str_state = False
        if type(bytes_data) == str:
            bytes_data = bytes_data.encode()
            bytes_data_str_state = True
        for base, kwargs in mode_dict.items():
            bytes_data = base(bytes_data, **kwargs)
        return bytes_data.decode() if bytes_data_str_state else bytes_data

    def parser_plist(self, parser_dict: dict | None = None, out_file: str | None = None, **kwargs) -> bytes:
        """
        将 dict 解析为 .plist
        这里可能需要自己在处理一下 因为 保存的文件的编码问题等
        :param parser_dict: 被解析的 dict 默认为解析 self.plist_dict
        :param out_file: 输出解析数据到指定文件 默认不输出 文件
        :param kwargs: plistlib.dumps 扩展参数
        :return: 已解析 plist 数据

        parser_dict 为默认参数时 会使用 self.parser_dict
        调用本方法会直接 刷新 self.plist_data

        """
        parser_dict = self.plist_dict if parser_dict == None else parser_dict
        if parser_dict == None:
            raise KeyError('parser_dict 数据为空 或者不符合执行要求 不能执行此操作')
        parser_plist = plistlib.dumps(parser_dict, **kwargs)
        if out_file:
            with open(out_file, 'wb') as out_file:
                out_file.write(parser_plist)
        self.plist_data = parser_plist  # 更新实例的解析数据
        # return parser_plist.decode()  # 这里 self.plist_data 是没有解码的 bytes 数据 然后这个位置返回看情况解码
        return parser_plist  # 这里 是没有解码的 bytes 数据 节省性能开支

    def parser_dict(self, parser_plist: str | None = None, **kwargs) -> dict:
        """
        将 .plist 解析为 dict
        :param parser_plist: 给定解析的 .plist 文件 或者 二进制 或者 文本 数据
        :param kwargs: plistlib.load 扩展参数
        :return: 已解析 dict 数据

        parser_plist 为默认参数时 会使用 self.plist_data
        调用本方法会直接 刷新 self.plist_dict

        """
        parser_plist = self.plist_data if parser_plist == None else parser_plist
        if parser_plist == None:
            raise KeyError('parser_plist 数据为空 或者不符合执行要求 不能执行此操作')
        if os.path.isfile(parser_plist):  # 这里使用判断文件是否存在的方法来判定 如果文件不存在且他是文件则可能出现 识别为 文件内容数据的情况
            with open(parser_plist, 'rb') as parser_plist:
                parser_dict = plistlib.load(parser_plist, **kwargs)
        else:
            parser_plist = parser_plist.encode() if type(parser_plist) != bytes else parser_plist
            parser_dict = plistlib.loads(parser_plist, **kwargs)
        self.plist_dict = parser_dict  # 更新实例的解析数据
        return parser_dict

    def customization_parser_dict_value(self, value_path: tuple,
                                        cust_value: str | int | bytes | list | dict | None = None,
                                        cust_value_all: bool = False) -> str | int | bytes | list | dict | tuple | None:
        """
        提供 基础 自定义 parser_dict 值功能
        :param value_path: 一个元组 元组中的数据从左到右顺序 表达 需要修改 或者查询数据位置
        :param cust_value: 自定义(修改)的数据 默认则不修改 仅查询 当该参数为 bool对象时 则为删除操作
        :param cust_value_all: 是否无论 cust_value 为任何使用值都 执行数据更新操作(即增改操作)
        :return: value_path 指定位置的数据 或者修改后数据  如果返回数据为None说明没有找到找到的数据(也有可能是该数据本身就是None但这里不允许使用直接的None对象做plist数据)


        这里解释一下 value_path 这个路径
        他是一个元组 路径顺序是从左到右 分别对应 dict 的key
        列如 {'a':2, 'b':{'c':3}} 中的 c key 的值是3 则 c那个key的路径就是:
        ('b','c')
        这样子 很简单

        """
        plist_dict_value = self.plist_dict
        if plist_dict_value == None:
            raise KeyError('parser_plist 数据为空 或者不符合执行要求 不能执行此操作')
        value_path_len = len(value_path)
        value_path_last = value_path_len - 1
        for index in range(value_path_len):
            value_path_index = value_path[index]
            if index == value_path_last and (cust_value != None or cust_value_all):
                if type(cust_value) == bool and cust_value_all == False:
                    try:
                        plist_dict_value.pop(value_path_index)
                    except KeyError:
                        pass
                else:
                    plist_dict_value[value_path_index] = cust_value
            try:  # 这里原来是用 if plist_dict.get的 但是这种方法在 value为None时有一定问题
                plist_dict_value = plist_dict_value[value_path_index]
            except KeyError:
                return
        return plist_dict_value

    def customization_parser_dict_values(self, cust_dict: dict | None = None, cust_dict_all: bool = False,
                                         plist_dict: dict | None = None) -> dict:
        """
        提供 高级 批量 自定义/查询 parser_dict 值功能
        !!!使用 递归 方式实现
        :param cust_dict: 自定义(修改)的数据 | key-value value为None时则为 查询 | value为bool对象时则为 删除
        :param cust_dict_all: 是否无论 cust_value 为任何使用值都 执行数据更新操作(即增改操作)
        :param plist_dict: 本函数使用的 plist_dict 主要为 递归准备 一般情况下 该参数默认即可
        :return: 执行 cust_dict 后的返回数据 如查询数据等  (返回的字典 对应的value 为None时说明没有找到数据或者数据本身为None)

        PlistParser.customization_parser_dict_values 默认参数时:
        cust_dict: 默认使用 self.cust_dict
        plist_dict: 默认可以不管这个参数
        这里 详细解释一下 cust_dict 的 定义和含义
            cust_dict 是一个字典 其中:
                {
                    'key':'value',
                    'key2':{
                        'key3':value,
                        'key4':value,
                    },
                }
                这里其实就是一个正常的字典
                该字典在 PlistParser.customization_parser_dict_values 内容意义:
                    key:
                        对应 解析字典(self.plist_dict)的对应位置的key
                    value:
                        对应 解析字典(self.plist_dict)对应位置的value
                        当该值为 None 时 NoneType类型None 则为 查询 (所有查询的数据 会按顺序排列为字典返回[其数据结构与cust_dict相仿])
                        当该值为 bool对象(False, True)时则为 删除该数据
                        当该值不存在 则创建

        """
        cust_dict = self.cust_dict if cust_dict == None else cust_dict
        plist_dict = self.plist_dict if plist_dict == None else plist_dict
        not_cust_dict_all = not cust_dict_all
        print(cust_dict_all)
        inquire_dict = {}
        if cust_dict == None:
            raise KeyError('cust_dict 数据为空 或者不符合执行要求 不能执行此操作')
        for plist_dict_index, cust_value in cust_dict.items():
            cust_value_type = type(cust_value)
            if cust_value_type == dict:
                inquire_dict_item = self.customization_parser_dict_values(cust_value, cust_dict_all,
                                                                          plist_dict[plist_dict_index])
                if inquire_dict_item:
                    inquire_dict[plist_dict_index] = inquire_dict_item
            elif cust_value == None and not_cust_dict_all:
                try:  # 这里原来是用 if plist_dict.get的 但是这种方法在 value为None时有一定问题
                    plist_dict_value = plist_dict[plist_dict_index]
                except KeyError:
                    plist_dict_value = None
                inquire_dict[plist_dict_index] = plist_dict_value
            elif cust_value_type == bool and not_cust_dict_all:
                try:
                    plist_dict.pop(plist_dict_index)
                except KeyError:
                    pass
            else:
                plist_dict[plist_dict_index] = cust_value
        return inquire_dict

    def plist_dict_to_cust_dict(self, plist_dict: dict) -> dict:
        """
        将 Plist dict 数据 转换 标准 cust dict
        :param plist_dict: 需要 转换的 plist dict 数据
        :return: 完成 转换的 cust dict 数据

        因为 PlistParser.plist_dict_to_cust_dict 是为了方便 调用 PlistParser.customization_parser_dict_values
            所以 执行该函数会更新 self.cust_dict  在调用 PlistParser.customization_parser_dict_values 时 默认会使用 self.cust_dict
        这里介绍一下 plist_dict 和 cust_dict
        plist_dict:
            {
            path_value: value,
            path_value: value,
            ...,
            }
            path_value:
                与PlistParser.customization_parser_dict_values 中的 path_value 一样的参数
            value:
                值 与PlistParser.customization_parser_dict_values 中的 cust_value 差不多
        cust_dict:
            cust_dict 是一个字典 其中:
                {
                    'key':'value',
                    'key2':{
                        'key3':value,
                    },
                }
                这里其实就是一个正常的字典
                该字典在 PlistParser.customization_parser_dict_values 内容意义:
                    key:
                        对应 解析字典(plist_parser.plist_dict)的对应位置的key
                    value:
                        对应 解析字典(self.plist_dict)对应位置的value
                        当该值为 None 时 NoneType类型None 则为 查询 (所有查询的数据 会按顺序排列为字典返回[其数据结构与cust_dict相仿])
                        当该值为 bool对象(False, True)时则为 删除该数据
                        当该值不存在 则创建

        """
        cust_dict = {}
        for plist_key, cust_value in plist_dict.items():
            cust_dict_index = cust_dict
            plist_key_len = len(plist_key)
            plist_key_last = plist_key_len - 1
            for index in range(plist_key_len):
                plist_key_index = plist_key[index]
                if index == plist_key_last:
                    cust_dict_index[plist_key_index] = cust_value
                    break
                if cust_dict_index.get(plist_key_index) == None:
                    cust_dict_index[plist_key_index] = {}
                cust_dict_index = cust_dict[plist_key_index]
        self.cust_dict = cust_dict
        return cust_dict
