from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name='fnmatch_patch',
    ext_modules=cythonize(["fnmatch_patch.pyx"]),
    cmdclass={'build_ext': build_ext, 'inplace': True},
    requires=['Cython'],
    version='1.0.0',
    description='Replace python fnmatch with GNU C fnmatch',
    author='asimuskov@intermedia.net',
    author_email='asimuskov@intermedia.net',
    long_description='Replace python fnmatch with GNU C fnmatch',
)
