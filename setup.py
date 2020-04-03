#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ast
import io
import re
import os
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

def load_requirements(fname):
    try:
        from pip._internal.req import parse_requirements
    except ImportError:
        from pip.req import parse_requirements
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setup(
    name="pdf2docx",
    description="Parse PDF files to docx",
    version="0.0.1",
    author="https://dothinking.github.io/blog/",
    author_email="https://dothinking.github.io/blog/",
    url="https://github.com/uklfr/pdf2docx",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points={"console_scripts": ["pdf2docx=pdf2docx.command_line:main"]},
    zip_safe=False,
    install_requires=load_requirements("requirements.txt"),
    python_requires=">=3.6",
    license="License :: Unknown",
)
