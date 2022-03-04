from setuptools import setup, find_packages
from pathlib import Path
import codecs
import os

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.4'
DESCRIPTION = 'Package for the Authify.biz API'

setup(
    name="Authify",
    version=VERSION,
    author="Clynt",
    author_email="<mail@clynt.me>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'pycryptodome', 'fingerprint'],
    keywords=['wrapper', 'apiwrapper', 'authify', 'auth', 'authsystem'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
