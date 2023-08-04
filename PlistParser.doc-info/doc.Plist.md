---

 文件名称: Plist.md
 文件创建时间: 2023/7/12
 源作者: [EelsYikes-White]
 附作者: [...]
 
---
# Plist 库介绍

`PlistParser 包中 Plist库 提供了 对Plist数据结构相关支持` 

---


## PlistItem对象 提供的属性和方法:
* PlistItem.name
  * 该属性提供 该属性的名称 就是属性名称的 str 字符
* PlistItem.item_index_tuple
  * 该属性提供一个py 元组 元组顺序从左到右 分别表示在该节点在Plist中的路径
* PlistItem.item
  * 该属性是该节点 的真正名称
* PlistItem.item_index_head
  * 该属性是在拼接  dict路径时 会插入dict路径最前面的 str
* PlistItem.data
  * 该属性是该节点的值
* PlistItem.dict
  * 该属性 转换为标准的dict 提供操作 PlistParser的能力
* PlistItem.dict_index
  * 该属性为在标准dict中 该节点的 取值位置 是一个str表示的位置
* PlistItem.path
  * 该属性是 当前节点的路径 但是 和前面的路径表示方式不同 这里的路径 使用 . 来表示路径 且是一个str .的原因可能出现不兼容情况 建议尽可能 避免使用
* PlistItem.path_tuple
  * 该属性提供一个py 元组 元组顺序从左到右 分别表示在该节点在Plist中的路径 与 Plist.item_index_tuple 可能存在一定差异 没有差异那就无所谓了

---
## PlistItem对象 提供的运算(即提供的便捷操作方式)
* +PlistItem
  * 返回一个 可以用于字典取值的 str 路径
* -PlistItem
  * 返回 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict 数据
* ~PlistItem
  * 返回 当前节点的路径 以 元组 表达的 节点路径
* PlistItem + `这里可以是 元组 或者 列表 或者 字典`
  * 提供 对目标 数据 进行  结合 将当前节点插入 找到的运算参数中 不会改动self数据
* PlistItem - `这里是dict`
  * 提供 对目标 数据 进行 去除 将当前节点去除 找到的运算参数中  不会改动self数据
* PlistItem * `保存的文件(和open那个函数的文件参数一样)`
  * 提供 保存当前 节点为 文件 格式为标准的 .py 文件

---
## PlistItem对象 提供的方法(即提供的API)
* PlistItem(item_index_tuple, item, data=None, item_index_head='')
  * 创建 初始化一个PlistItem对象 
  * ```
    :param item_index_tuple:
    :param item: 当前节点在 .plist 中的名称 (key值)
    :param data: 当前节点的数据
    :param item_index_head: 当前节点的 前缀头数据 在  __pos__ __neg__ __invert__ 中引用拼接 节点路径前缀
    ```
* PlistItem.update(item_index_tuple=None, item=None, data=None, item_index_head=None)
  * 更新该实例(该节点)相关属性和数据
  * ```
    :param item_index_tuple:
    :param item: 当前节点在 .plist 中的名称 (key值)
    :param data: 当前节点的数据
    :param item_index_head: 当前节点的 前缀头数据 在  __pos__ __neg__ __invert__ 中引用拼接 节点路径前缀
    :return:
    ```
* PlistItem.simplification_dict(plist_dict=None)
  * 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict
  * ``` 
    :param plist_dict: 指定该参数 则 会将 解析的dict数据更新在 指定的 plist_dict 中
    :return: 完成解析的 dict
    ```
* PlistItem.dict_key_replacement(replacement_dict, mapping_dict, key_error=None)
  * 在 mapping_dict 中查找 replacement_dict 对应的 key 的替换值 并将其替换
  * ````
    :param replacement_dict: key 被替换的 dict
    :param mapping_dict:  替换 key 的映射 dict
    :return:
    ````
* PlistItem.attribute_mapping_dict(attribute_mapping_dict=None)
  * 分析并返回当前节点以及下级节点的 attribute_mapping_dict
  * ```
    :param attribute_mapping_dict: 上级 attribute_mapping_dict 默认情况下为回调使用 默认参数即可
    :return:
    ```
* PlistItem.attribute_mapping_dict_reverse(attribute_mapping_dict):
  * 颠倒 attribute_mapping_dict_reverse 的 key 和 value
  * ```
    :param attribute_mapping_dict: 被颠倒 key value 的 attribute_mapping_dict
    :return:
    ```
* PlistItem.load_parse_dict(load_dict, attribute_mapping_dict, index_tuple=None, class_item_obj=None, key_error=None)
  * 提供将 parse_dict  插入 并更新到 此节点 会直接改变 self的数据
  * ```
    :param load_dict:  需要插入当前节点的 parse_dict
    :param attribute_mapping_dict:  属性映射表
    :param index_tuple:  路径 以元组为表达方式
    :param key_error:  当出现 attribute_mapping_dict 找不到指定的key 时 是否自动跳过
    :return: 当前节点 self
     ```
* PlistItem.save_py_file(self, type_index=None)
  * 将当前节点及以下节点 转换为 标准 的py文件 提供 永久的py源码存储方式
  * 此方法无法直接保存文件 而是 会返回 符合 py语法的 字符数据
  * 该方法使用递归实现
  * ```
    :param type_index: 默认调用时不用管这个参数 主要是留给 递归 验证 是否已经存在 一个 class 定义 防止 除非 定义
    :return:
    ```


---
# 应用 实例介绍
`Plist 设计的初衷是对接 PlistParser`
`使 PlistParser 变得简单易用 且强大`
`使用 Plist 需要联动 PlistParser 才能最大化其作用和优点长处`

---


## 基本应用
```python

from PlistParser.Plist import PlistItem

plist = PlistItem((),'plist')  # 创建一个plist 节点

print(+plist)  # 输出字典[]取值str代码
print(-plist)  # 输出PlistParser解析器支持的dict
print(~plist)  # 输出 当前节点的路径 以元组的方式(也是PlistParser解析器支持的元组路径)
print(plist + {})  # 下面进行 插入操作 不会影响 plist原来的数据
print(plist + ())
print(plist + [])
print(plist - {})  # 下面进行 去除操作 不会影响 plist原来的数据 这个操作只对dict有效
plist * '.py文件的路径'  # 讲 plist另存为 .py的操作

plist.update((),'','')  # 动态更新这个节点的属性
print(plist.simplification_dict())  # 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict
print(-plist)
print(plist.save_py_file())  # 将当前节点及以下节点 转换为 标准 的py文件内容 数据内容会返回 而不是直接写入文件

plist.load_parse_dict({},{})  # 提供将 parse_dict  插入 并更新到 此节点 会直接改变 self的数据
"""
上面这个 plist.load_parse_dict
plist.load_parse_dict -> PlistItem.load_parse_dict
其中 
load_dict 与 attribute_mapping_dict :
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

```

## 扩展应用
```python

"""
为了方便我们操作和永久化存储pyplist
我们使用自定义plist 但是这个plist是py版本的 基于.py文件和语法的plist 所以也可以称为pyplist
"""

from PlistParser.Plist import PlistItem

class PlistCacheExtraItem(PlistItem):
    pass
class PlistCacheExtra(PlistItem):
    def __init__(self, item_index_tuple, item, item_index_head=''):
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
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
        super().__init__(item_index_tuple, item, item_index_head=item_index_head)
        self.CacheUUID = PlistItem(item_index_tuple, 'CacheUUID')
        self.CacheData = PlistItem(item_index_tuple, 'CacheData')
        self.CacheVersion = PlistItem(item_index_tuple, 'CacheVersion')
        self.CacheExtra = PlistCacheExtra(('CacheExtra',), 'CacheExtra')


"""
这里我自定义了一个plist的pyplist
注意: 所有的pyplist都必须继承自PlistItem 包括pyplist的节点
就如上面实列的这样
"""

plist = Plist()

print(+plist)  # 输出字典[]取值str代码
print(-plist)  # 输出PlistParser解析器支持的dict
print(~plist)  # 输出 当前节点的路径 以元组的方式(也是PlistParser解析器支持的元组路径)
print(plist + {})  # 下面进行 插入操作 不会影响 plist原来的数据
print(plist + ())
print(plist + [])
print(plist - {})  # 下面进行 去除操作 不会影响 plist原来的数据 这个操作只对dict有效
plist * '.py文件的路径'  # 讲 plist另存为 .py的操作

plist.update((),'','')  # 动态更新这个节点的属性
print(plist.simplification_dict())  # 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict
plist.load_parse_dict({},{})  # 提供将 parse_dict  插入 并更新到 此节点 会直接改变 self的数据
print(-plist)
print(plist.save_py_file())  # 将当前节点及以下节点 转换为 标准 的py文件内容 数据内容会返回 而不是直接写入文件

```




