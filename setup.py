import re
import os
import glob
import shutil
from setuptools import setup, find_packages

PKG_PYRA2YR = "pyra2yr"
PKG_RA2YRPROTO = "ra2yrproto"

setup(
    name=PKG_PYRA2YR,
    version="0.0.1",
    description="RA2YR Python interface",
    url="",
    license="GPLv3",
    packages=find_packages(),
    data_files=[
        (PKG_RA2YRPROTO, glob.glob(os.path.join(PKG_RA2YRPROTO, "*.pyi")))
    ],
    package_dir={PKG_PYRA2YR: PKG_PYRA2YR, PKG_RA2YRPROTO: PKG_RA2YRPROTO},
    entry_points={
        "console_scripts": ["{n}={n}.main:main".format(n=PKG_PYRA2YR)]
    },
)
