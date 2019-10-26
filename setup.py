from distutils.core import setup

import setuptools
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name='cfnmatch',
    ext_modules=cythonize(["cfnmatch.pyx"]),
    cmdclass={'build_ext': build_ext, 'inplace': True},
    requires=['Cython'],
    python_requires='>=3.5',
    version='1.0.0',
    description='Replace python fnmatch with GNU C fnmatch',
    author='asimuskov',
    author_email='asimuskov@intermedia.net, opiumofthepeople@yandex.ru',
    url='https://github.com/an-death/cfnmatch',
    long_description='Replace python fnmatch with GNU C fnmatch',
    platforms=['*nix'],
    packages=setuptools.find_packages(),
)
