from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='fnmatch_patch',
    ext_modules=cythonize(["c_fnmatch.pyx"]), requires=['Cython'],
    version='1.0.0',
    description='Replace python fnmatch with GNU C fnmatch',
    author='asimuskov@intermedia.net',
    author_email='asimuskov@intermedia.net',
    long_description='Replace python fnmatch with GNU C fnmatch',
    include_package_data=True,
    zip_safe=False,
)
