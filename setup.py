# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# single-sourcing the version
with open(path.join(here, 'pyroyale/_version.py')) as f:
    exec(f.read())

setup(
    name='pyroyale',

    # Version single-sourced from pyroyale/_version.py
    version=__version__,

    description='Clash Royale API wrapper for Python 3',
    long_description=long_description,
    url='https://github.com/AaronTraas/pyroyale',
    author='Aaron Traas',
    author_email='aaron@traas.org',
    license='LGPLv3+',
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='ClashRoyale',

    packages=find_packages(exclude=['tests']),

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests'],
    tests_requires=['pytest','pytest-runner','coverage','requests_mock'],

    include_package_data=True,

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/AaronTraas/pyroyale/issues',
        'Source': 'https://github.com/AaronTraas/pyroyale',
    },
)
