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
        """
        bytes_data_str_state = False
        if type(bytes_data) == str:
            bytes_data.encode()
            bytes_data_str_state = True
        for base, kwargs in mode_dict.items():
            bytes_data = base(bytes_data, **kwargs)
        return bytes_data.decode() if bytes_data_str_state else bytes_data

    def parser_plist(self, parser_dict: dict | None = None, out_file: str | None = None, **kwargs) -> bytes:
        """
        将 dict 解析为 .plist
        :param parser_dict: 被解析的 dict 默认为解析 self.plist_dict
        :param out_file: 输出解析数据到指定文件 默认不输出 文件
        :param kwargs: plistlib.dumps 扩展参数
        :return: 已解析 plist 数据
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
                                        cust_value: str | None = None) -> str | bytes | list | dict:
        """
        提供 基础 自定义 parser_dict 值功能
        :param value_path: 一个元组 元组中的数据从左到右顺序 表达 需要修改 或者查询数据位置
        :param cust_value: 自定义(修改)的数据 默认则不修改 仅查询
        :return: value_path 指定位置的数据 或者修改后数据
        """
        plist_dict_value = self.plist_dict
        if plist_dict_value == None:
            raise KeyError('parser_plist 数据为空 或者不符合执行要求 不能执行此操作')
        value_path_len = len(value_path)
        value_path_last = value_path_len - 1
        for index in range(value_path_len):
            value_path_index = value_path[index]
            if index == value_path_last and cust_value:
                plist_dict_value[value_path_index] = cust_value
            plist_dict_value = plist_dict_value[value_path_index]
        return plist_dict_value

    def customization_parser_dict_values(self, cust_dict: dict | None = None, plist_dict: dict | None = None) -> dict:
        """
        提供 高级 批量 自定义/查询 parser_dict 值功能
        !!!使用 递归 方式实现
        :param cust_dict: cust_dict: 自定义(修改)的数据 | key-value value为 None 时 则为 查询
        :param plist_dict: 本函数使用的 plist_dict 主要为 递归准备 一般情况下 该参数默认即可
        :return: 执行 cust_dict 修改后的 数据
        """
        cust_dict = self.cust_dict if cust_dict == None else cust_dict
        plist_dict = self.plist_dict if plist_dict == None else plist_dict
        inquire_dict = {}
        if cust_dict == None:
            raise KeyError('cust_dict 数据为空 或者不符合执行要求 不能执行此操作')
        for plist_dict_index, cust_value in cust_dict.items():
            if type(cust_value) == dict:
                inquire_dict_item = self.customization_parser_dict_values(cust_value, plist_dict[plist_dict_index])
                if inquire_dict_item:
                    inquire_dict[plist_dict_index] = inquire_dict_item
                continue
            elif cust_value == None:
                inquire_dict[plist_dict_index] = plist_dict[plist_dict_index]
            else:
                plist_dict[plist_dict_index] = cust_value
        return inquire_dict

    def plist_dict_to_cust_dict(self, plist_dict: dict) -> dict:
        """
        将 Plist dict 数据 转换 标准 cust dict
        :param plist_dict: 需要 转换的 plist dict 数据
        :return: 完成 转换的 cust dict 数据
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


class FastPlistParser(PlistParser):

    def __init__(self, parser_plist: str | dict | PlistParser | None = None, auto_parser: bool = True,
                 cust_dict: dict = None,
                 *args, **kwargs):
        """

        :param parser_plist: 给定解析的 .plist 文件 或者 二进制 或者 文本 数据
        :param auto_parser: 是否在 plist_txt 不为空时 自动在初始化时解析 plist_txt (在 plist_txt 为空时 该参数不会有任何效果)
        :param cust_dict: 全称 customization_dict 给定自定义的 plist 字典数据
        """
        if type(parser_plist) == PlistParser:
            super().__init__()
            self.__dict__ = parser_plist.__dict__
        else:
            # super().__init__(parser_plist, auto_parser, cust_dict, *args, **kwargs)
            super().__init__(parser_plist, auto_parser, cust_dict)

    def device_model(self, set_value: str | bytes | list | dict | None = None) -> str | bytes | list | dict | None:
        """
        一键 查询/设置 设备型号
        :param set_value: 自定义(修改)的数据 默认则不修改 仅查询
        :return: 设备数据 或者修改后数据
        """
        plist_dict = self.plist_dict
        if plist_dict == None:
            raise KeyError('self.plist_dict 数据为空 或者不符合执行要求 不能执行此操作')
        plist_dict = plist_dict["CacheExtra"]
        if set_value:
            plist_dict["Z/dqyWS6OZTRy10UcmUAhw"] = set_value
        return plist_dict["Z/dqyWS6OZTRy10UcmUAhw"]

    def device_category(self, set_value: str | bytes | list | dict | None = None) -> str | bytes | list | dict | None:
        """
        一键 查询/设置 设备类别
        :param set_value: 自定义(修改)的数据 默认则不修改 仅查询
        :return: 设备数据 或者修改后数据
        """
        plist_dict = self.plist_dict
        if plist_dict == None:
            raise KeyError('self.plist_dict 数据为空 或者不符合执行要求 不能执行此操作')
        plist_dict = plist_dict["CacheExtra"]
        if set_value:
            plist_dict["VuGdqp8UBpi9vPWHlPluVQ"] = set_value
        return plist_dict["VuGdqp8UBpi9vPWHlPluVQ"]

    def device_issuance(self, set_value: str | bytes | list | dict | None = None) -> str | bytes | list | dict | None:
        """
        一键 查询/设置 设备发行
        :param set_value: 自定义(修改)的数据 默认则不修改 仅查询
        :return: 设备数据 或者修改后数据
        """
        plist_dict = self.plist_dict
        if plist_dict == None:
            raise KeyError('self.plist_dict 数据为空 或者不符合执行要求 不能执行此操作')
        plist_dict = plist_dict["CacheExtra"]
        if set_value:
            plist_dict["zHeENZu+wbg7PUprwNwBWg"] = set_value
        return plist_dict["zHeENZu+wbg7PUprwNwBWg"]

    def device_system(self, set_value: str | bytes | list | dict | None = None) -> str | bytes | list | dict | None:
        """
        一键 查询/设置 设备系统
        :param set_value: 自定义(修改)的数据 默认则不修改 仅查询
        :return: 设备数据 或者修改后数据
        """
        plist_dict = self.plist_dict
        if plist_dict == None:
            raise KeyError('self.plist_dict 数据为空 或者不符合执行要求 不能执行此操作')
        plist_dict = plist_dict["CacheExtra"]
        if set_value:
            plist_dict["ivIu8YTDnBSrYv/SN4G8Ag"] = set_value
        return plist_dict["ivIu8YTDnBSrYv/SN4G8Ag"]



