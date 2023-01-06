# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in apollo/__init__.py
from apollo import __version__ as version

setup(
	name="apollo",
	version=version,
	description="Custom App for Apollo Tyres",
	author="Neil Lasrado",
	author_email="neil@switchon.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
