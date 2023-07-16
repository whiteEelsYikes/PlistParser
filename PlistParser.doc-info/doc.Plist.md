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
* PlistItem(self, item_index_tuple, item, data=None, item_index_head='')
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
* PlistItem.simplification_dict(self, plist_dict=None)
  * 将当前节点以及下级节点 转换为 PlistParser 解析器 接受的 dict
  * ``` 
    :param plist_dict: 指定该参数 则 会将 解析的dict数据更新在 指定的 plist_dict 中
    :return: 完成解析的 dict
    ```
* PlistItem.load_parse_dict(self, load_dict, attribute_mapping_dict, index_tuple=None, class_item_obj=None, key_error=None)
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
## 应用 实例介绍

---








