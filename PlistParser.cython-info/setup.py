

'''

 !! 实验程序 不保证正确性

'''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        'PlistParser',
        ['./../PlistParser/*.py']
    ),

]

setup(
    name='test',
    ext_modules=cythonize(extensions),
)