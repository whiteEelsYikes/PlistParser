#!/usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import os
import plistlib

import setuptools  # 导入setuptools打包工具
from distutils.extension import Extension
from Cython.Build import cythonize

import PlistParser


# with open('requires.txt', 'w', encoding='utf-8') as requires:
#     requires_txt = [item+'\n' for item in PlistParser.__requires_all__]
#     requires.write(''.join(requires_txt))

with open('README.md', 'r', encoding='utf-8') as README_md:
    long_description = README_md.read()


setuptools.setup(
    name='PlistParser',  # 项目名称
    version=PlistParser.__version__,  # 包版本号，便于维护版本
    url=r'https://github.com/whiteEelsYikes/PlistParser',  # 自己项目地址，比如github的项目地址
    author=r'white-EelsYikes',  # 作者，可以写自己的姓名
    author_email=r'2172989337@qq.com',  # 作者联系方式，可写自己的邮箱地址
    description='Extension package for .plist file parsing',  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',  # 3 - Alpha | 4 - Beta | 5 - Production/Stable
        'Intended Audience :: Developers',  # 开发的目标用户
        'Topic :: Software Development :: Build Tools',  # 属于什么类型
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['Plist', 'PlistParser'],
    platforms=['Windows', 'Linux', 'MacOS'],
    python_requires='>=3.6',  # 对python的最低版本要求
    install_requires=[
        # 'os',
        # 'Base64',
        # 'plistlib',
    ],  # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    packages=setuptools.find_packages(),
    # ext_modules=cythonize(
    #     module_list=[
    #         "PlistParser/*.py",
    #         # os.__file__,
    #         # base64.__file__,
    #         # plistlib.__file__
    #     ],
    #     language_level=3,)

)
