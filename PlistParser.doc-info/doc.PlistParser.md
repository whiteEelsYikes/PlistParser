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
* PlistParser.customization_parser_dict_value(value_path, cust_value=None)
  * 提供 基础 自定义 parser_dict 值功能 
  * ```
    :param value_path: 一个元组 元组中的数据从左到右顺序 表达 需要修改 或者查询数据位置
    :param cust_value: 自定义(修改)的数据 默认则不修改 仅查询
    :return: value_path 指定位置的数据 或者修改后数据
    ```
* PlistParser.customization_parser_dict_values(cust_dict=None, plist_dict=None)
  * 提供 高级 批量 自定义/查询 parser_dict 值功能
  * !!!使用 递归 方式实现   
  * ```
    :param cust_dict: cust_dict: 自定义(修改)的数据 | key-value value为 None 时 则为 查询
    :param plist_dict: 本函数使用的 plist_dict 主要为 递归准备 一般情况下 该参数默认即可
    :return: 执行 cust_dict 修改后的 数据
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

















