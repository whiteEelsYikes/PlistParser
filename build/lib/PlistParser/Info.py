#!/usr/bin/python3
# -*- coding: utf-8 -*-


__version__ = '2023.7.28.0'

__build_peoples__ = {
    r'white-EelsYikes': '2172989337@qq.com',
}

__license_body__ = \
    """
    + --------------------------------------------------------------------------------- +
    *   MIT License                                                                     *
    *                                                                                   *
    *   Copyright (c) 2023 white-EelsYikes                                              *
    *                                                                                   *
    *   Permission is hereby granted, free of charge, to any person obtaining a copy    *
    *   of this software and associated documentation files (the "Software"), to deal   *
    *   in the Software without restriction, including without limitation the rights    *
    *   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       *
    *   copies of the Software, and to permit persons to whom the Software is           *
    *   furnished to do so, subject to the following conditions:                        *
    *                                                                                   *
    *   The above copyright notice and this permission notice shall be included in all  *
    *   copies or substantial portions of the Software.                                 *
    *                                                                                   *
    *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      *
    *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        *
    *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     *
    *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          *
    *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   *
    *   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   *
    *   SOFTWARE.                                                                       *
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
"""
__license_head__ = \
    """\033[5;40;32m
    \033[5;40;32m+-----------------------------------------------------------------------------------+
    \033[5;40;32m+\033[5;40;31m  ███╗   ███╗██╗████████╗    ██╗     ██╗ ██████╗███████╗███╗   ██╗███████╗███████╗ \033[5;40;32m+
    \033[5;40;32m+\033[5;40;31m  ████╗ ████║██║╚══██╔══╝    ██║     ██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝ \033[5;40;32m+
    \033[5;40;32m+\033[5;40;31m  ██╔████╔██║██║   ██║       ██║     ██║██║     █████╗  ██╔██╗ ██║███████╗█████╗   \033[5;40;32m+
    \033[5;40;32m+\033[5;40;31m  ██║╚██╔╝██║██║   ██║       ██║     ██║██║     ██╔══╝  ██║╚██╗██║╚════██║██╔══╝   \033[5;40;32m+
    \033[5;40;32m+\033[5;40;31m  ██║ ╚═╝ ██║██║   ██║       ███████╗██║╚██████╗███████╗██║ ╚████║███████║███████╗ \033[5;40;32m+
    \033[5;40;32m+\033[5;40;31m  ╚═╝     ╚═╝╚═╝   ╚═╝       ╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝ \033[5;40;32m+\
    """

__license__ = f'{__license_head__}{__license_body__}'

def open_project_link(project_link=r'https://github.com/whiteEelsYikes/PlistParser'):
    """
    使用电脑默认链接打开程序 打开指定的项目链接
    :param project_link:
    :return:
    """
    import webbrowser  # 这里 py 是有优化的 已经存在的库 再次执行导入是无效的 除非使用异步导入 重载已导入的库
    webbrowser.open(project_link)

