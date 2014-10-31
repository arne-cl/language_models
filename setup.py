#!/usr/bin/env python
 
import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
 
here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README.rst')).read()
 
setup(name='language_models',
version='0.1.0',
description='language models implemented in Python',
#long_description=README,
author='Arne Neumann',
author_email='languagemodels.programming@arne.cl',
url='https://github.com/arne-cl/language_models',
package_dir={'language_models': ''},
packages={'language_models'},
#py_modules=['discoursekernels'],
#scripts=['spectrum_kernel.py', 'subsequence_kernels.py', 'tree_kernel.py'],
license='3-Clause BSD',
#install_requires=['networkx', 'numpy', 'repoze.lru', 'ordered_set'],
)
