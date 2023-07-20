---

 文件名称: PlistParser.md
 文件创建时间: 2023/7/12
 源作者: [EelsYikes-White]
 附作者: [...]

---
# PlistParser 库介绍

`PlistParser 包中 PlistParser库 提供了 Plist解析和操作相关支持` 

---

## PlistParser对象 提供的属性和方法:
* PlistParser.plist_data
  * plist xml 的源数据 就是plist文件内容的str数据 相当于open读取后得到的数据
* PlistParser.plist_dict
  * plist 文件 转化后的 字典 
* PlistParser.cust_dict
  * 全称 customization_dict 该属性主要提供 给 PlistParser.customization_parser_dict_values API 使用

## PlistParser对象 提供的属性和方法:
* `暂未提供`

## PlistParser对象 提供的方法(即提供的API)
* PlistParser(parser_plist=None, auto_parser=True, cust_dict=None)
  * 创建 初始化一个PlistParser对象 
  * ```
    :param parser_plist: 给定解析的 .plist 文件 或者 二进制 或者 文本 数据
    :param auto_parser: 是否在 plist_txt 不为空时 自动在初始化时解析 plist_txt (在 plist_txt 为空时 该参数不会有任何效果)
    :param cust_dict: 全称 customization_dict 给定自定义的 plist 字典数据
    ```
* PlistParser.parser_base64(bytes_data, mode_dict)
  * 提供强大的 base64 基础加解密支持 可支持嵌套加解密
  * (一开始传入的bytes_data是什么类型就返回什么类型)
  * ```
    :param bytes_data: 被这些操作的(加解密)数据
    :param mode_dict: 加解密操作及其参数声明字典
    :return: 执行 mode_dict 指定操作后的 加解密 数据
    ```
* PlistParser.parser_plist(parser_dict=None, out_file=None, **kwargs)
  * 将 dict 解析为 .plist
  * ```
    :param parser_dict: 被解析的 dict 默认为解析 self.plist_dict
    :param out_file: 输出解析数据到指定文件 默认不输出 文件
    :param kwargs: plistlib.dumps 扩展参数
    :return: 已解析 plist 数据
    ```
* PlistParser.parser_dict(parser_plist=None, **kwargs)
  * 将 .plist 解析为 dict
  * ```
     :param parser_plist: 给定解析的 .plist 文件 或者 二进制 或者 文本 数据
     :param kwargs: plistlib.load 扩展参数
     :return: 已解析 dict 数据
     ```
* PlistParser.customization_parser_dict_value(value_path, cust_value=None, cust_value_all=False)
  * 提供 基础 自定义 parser_dict 值功能 
  * ```
    提供 基础 自定义 parser_dict 值功能
    :param value_path: 一个元组 元组中的数据从左到右顺序 表达 需要修改 或者查询数据位置
    :param cust_value: 自定义(修改)的数据 默认则不修改 仅查询 当该参数为 bool对象时 则为删除操作
    :param cust_value_all: 是否无论 cust_value 为任何使用值都 执行数据更新操作(即增改操作)
    :return: value_path 指定位置的数据 或者修改后数据  如果返回数据为None说明没有找到找到的数据(也有可能是该数据本身就是None但这里不允许使用直接的None对象做plist数据)
    ```
* PlistParser.customization_parser_dict_values(cust_dict=None, cust_dict_all=False, plist_dict=None)
  * 提供 高级 批量 自定义/查询 parser_dict 值功能
  * !!!使用 递归 方式实现   
  * ```
    提供 高级 批量 自定义/查询 parser_dict 值功能
    !!!使用 递归 方式实现
    :param cust_dict: 自定义(修改)的数据 | key-value value为None时则为 查询 | value为bool对象时则为 删除
    :param cust_dict_all: 是否无论 cust_value 为任何使用值都 执行数据更新操作(即增改操作)
    :param plist_dict: 本函数使用的 plist_dict 主要为 递归准备 一般情况下 该参数默认即可
    :return: 执行 cust_dict 后的返回数据 如查询数据等  (返回的字典 对应的value 为None时说明没有找到数据或者数据本身为None)
    ```

* PlistParser.plist_dict_to_cust_dict(plist_dict)
  * 将 Plist dict 数据 转换 标准 cust dict
  * ```
    :param plist_dict: 需要 转换的 plist dict 数据
    :return: 完成 转换的 cust dict 数据
    ```
 

---
## 应用 实例介绍

---


## 基本应用
`参考上述介绍 进行以下应用:`
```python

from PlistParser.PlistParser import PlistParser


plist = r'plist/example.plist'
out_plist = r'plist/example.plist'


plist_parser = PlistParser()  # 创建一个解析器


dict = plist_parser.parser_dict(plist)  # 解析 指定的plist文件为dict
"""
每次执行 PlistParser.parser_dict 都会更新 PlistParser.plist_dict
"""
print(dict)
print(plist_parser.plist_dict)


plist = plist_parser.parser_plist()  # 将plist_parser.dict 解析为 plist
plist_ = plist_parser.parser_plist(dict)  # 将dict 解析为 plist
"""
每次执行 PlistParser.parser_plist 都会更新 PlistParser.plist_data
"""
print(plist)
print(plist_)


import base64     # 这里演示的是 plist_parser(PlistParser)嵌入的base64 加解密支持
from PlistParser.Base64 import Base64
base64_mode = {
    # 加解密操作函数 : {}  # 这个字典是 加解密操作函数的参数表(不能包括加解密数据的参数 因为PlistParser中会自动处理这个参数)
    base64.b64encode:{},  # 先执行 加密操作
    Base64.Decode.bit64:{},  # 在执行一次 解密操作
    Base64.Encode.bit32:{},  # 在执行一次 32bit的加密操作
}
base64_end = plist_parser.parser_base64('PlistParser', base64_mode)
print(base64_end)
base64_mode = {
    base64.b32decode:{},  # 执行 32bit 解密
}
base64_end = plist_parser.parser_base64(base64_end, base64_mode)
print(base64_end)




print('-'*100)  # 1这里开始演示 自定义或查询plist解析后 dict的值  方式: PlistParser.customization_parser_dict_value
value_path = ('CacheData', )  # 这里定义 我们目标值的路径
"""
这里解释一下 value_path 这个路径
他是一个元组 路径顺序是从左到右 分别对应 dict 的key
列如 {'a':2, 'b':{'c':3}} 中的 c key 的值是3 则 c那个key的路径就是:
('b','c')
这样子 很简单
"""
value = '自定义CacheData'
plist_parser.customization_parser_dict_value(value_path, value)  # 自定义值 当该值不存在时则 创建
value = plist_parser.customization_parser_dict_value(value_path, )  # 查询
print(value)
print(plist_parser.plist_dict)




print('='*100)  # 2这里开始演示 自定义或查询plist解析后 dict的值  方式:
cust_dict = {
    'CacheData': 'abcd',
    'CacheExtra': {
        'Z/dqyWS6OZTRy10UcmUAhw': None,
    }
}
"""
PlistParser.customization_parser_dict_values 默认参数时:
    cust_dict: 默认使用 PlistParser.cust_dict
    plist_dict: 默认可以不管这个参数
这里 详细解释一下 cust_dict 的 定义和含义
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
            对应 解析字典(plist_parser.plist_dict)对应位置的value
            当该值为 None 时 NoneType类型None 则为 查询 (所有查询的数据 会按顺序排列为字典返回[其数据结构与cust_dict相仿])
            当该值为 bool对象(False, True)时则为 删除该数据
            当该值不存在 则创建
"""
value_dict = plist_parser.customization_parser_dict_values(cust_dict,)
print(value_dict)




print('+'*100) # 这里演示转换器 plist_dict 转 cust_dict 这个操作存在的意义是为了 方便调用 plist_parser.customization_parser_dict_values
# PlistParser.plist_dict_to_cust_dict
plist_dict = {
    # 路径(与PlistParser.customization_parser_dict_value中的value_path是一样的) : 值
    ('CacheData',): 'abcd',
    ('CacheExtra', 'Z/dqyWS6OZTRy10UcmUAhw'): None,
}
"""
因为 PlistParser.plist_dict_to_cust_dict 是为了方便 调用 PlistParser.customization_parser_dict_values 
    所以 执行该函数会更新 PlistParser.cust_dict  在调用 PlistParser.customization_parser_dict_values 时 默认会使用 PlistParser.cust_dict
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
    这个就是PlistParser.customization_parser_dict_values的cust_dict
"""
cust_dict = plist_parser.plist_dict_to_cust_dict(plist_dict)
print(cust_dict)


```

## 扩展应用
```python



"""
为了方便我们自己的操作 我们可以专门定制 适合自己的解析器
可以使用继承重写等实现 如下:
并且我们为了方便 操作 定义 编辑 等操作 引入PlistItem 的自定义 Plist
"""

from PlistParser.PlistParser import PlistParser
from PlistParser.Plist import PlistItem

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


class PlistCacheExtraItem(PlistItem):
    pass


class PlistCacheExtra(PlistItem):
    def __init__(self, item_index_tuple, item, item_index_head=''):
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        item_index_tuple = ('CacheExtra', )
        self.device_category = PlistCacheExtraItem(item_index_tuple, 'VuGdqp8UBpi9vPWHlPluVQ',
                                                   item_index_head=item_index_head)
        self.device_issuance = PlistCacheExtraItem(item_index_tuple, 'zHeENZu+wbg7PUprwNwBWg',
                                                   item_index_head=item_index_head)
        self.device_model = PlistCacheExtraItem(item_index_tuple, 'Z/dqyWS6OZTRy10UcmUAhw',
                                                item_index_head=item_index_head)
        self.device_system = PlistCacheExtraItem(item_index_tuple, 'ivIu8YTDnBSrYv/SN4G8Ag',
                                                 item_index_head=item_index_head)


class Plist(PlistItem):
    """
    更新解析 self 可以 self.__dict__ 来实现  或者  type()
    """
    def __init__(self, item_index_tuple=None, item='Plist', data=None, item_index_head=''):
        item_index_tuple = () if item_index_tuple == None else item_index_tuple
        super().__init__(item_index_tuple, item, data, item_index_head=item_index_head)
        self.CacheUUID = PlistItem(item_index_tuple, 'CacheUUID')
        self.CacheData = PlistItem(item_index_tuple, 'CacheData')
        self.CacheVersion = PlistItem(item_index_tuple, 'CacheVersion')
        self.CacheExtra = PlistCacheExtra((), 'CacheExtra')




plist_txt = r'plist/example.plist'
out_plist = r'plist/example.plist'

plist = Plist()
plist_parser = FastPlistParser()
plist_parser.parser_dict(plist_txt)

# 此处 省略部分操作 实例 只列举 重点
data = plist_parser.customization_parser_dict_value(~plist.CacheExtra.device_issuance,False)  # 删除指定数据
print(data)
data = plist_parser.customization_parser_dict_value(~plist.CacheExtra.device_issuance)
print(data)


dict_ = {
    ~plist.CacheExtra.device_issuance:True,
    ~plist.CacheExtra.device_issuance:None,
}
plist_parser.plist_dict_to_cust_dict(dict_)
data = plist_parser.customization_parser_dict_values()
print(data)



```















