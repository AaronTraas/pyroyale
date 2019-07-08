# Always prefer setuptools over distutils
from setuptools import setup, find_packages  # noqa: H301
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# single-sourcing the version
with open(path.join(here, 'pyroyale/_version.py')) as f:
    exec(f.read())

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name='pyroyale',

    # Version single-sourced from pyroyale/_version.py
    version=__version__,

    description='Clash Royale API wrapper for Python 3',
    author='Aaron Traas',
    author_email='aaron@traas.org',
    license='LGPLv3+',
    url='https://github.com/AaronTraas/pyroyale',
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
    ],

    keywords=["Clash Royale"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/AaronTraas/pyroyale/issues',
        'Source': 'https://github.com/AaronTraas/pyroyale',
    },
)
