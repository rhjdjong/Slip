# Copyright (c) 2017 Ruud de Jong
# This file is part of the SlipLib project which is released under the MIT license.
# See https://github.com/rhjdjong/SlipLib for details.

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
import os.path


version_dict = {}
with open(os.path.join('src', 'sliplib', 'version.py')) as version_file:
    exec(version_file.read(), version_dict)
__version__ = version_dict['__version__']
del version_dict


# Get the long description from the relevant file
def read_long_description(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    seperator = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return seperator.join(buf)


long_description = read_long_description('README.rst')

TEST_REQUIRES = ['pytest', 'pytest-mock', 'pytest-cov']
DOC_REQUIRES = ['sphinx_rtd_theme']
DEV_REQUIRES = ['tox', 'mypy', 'wheel', 'twine']

setup(
    name='sliplib',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='Slip package',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/rhjdjong/SlipLib',

    # Author details
    author='Ruud de Jong',
    author_email='ruud.de.jong@xs4all.nl',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # What does your project relate to?
    keywords='slip message framing protocol RFC1055',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    package_dir={'': 'src'},
    packages=find_packages('src'),

    extras_require={
        'dev': DEV_REQUIRES + DOC_REQUIRES + TEST_REQUIRES,
        'test': TEST_REQUIRES
    }
)
