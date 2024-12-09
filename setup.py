#!/usr/bin/env python3

import pathlib

import setuptools

# The directory containing this file
CURR_DIR = pathlib.Path(__file__).parent

# The text of the README file
README = (CURR_DIR / "README.md").read_text()

setuptools.setup(
     name='iris_interface',
     version='1.2.0',
     packages=['iris_interface'],
     author="DFIR-IRIS - Airbus CyberSecurity",
     author_email="contact@dfir-iris.org",
     description="An interface for Iris modules",
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://github.com/dfir-iris/iris-module-interface",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: LGLP 3.0 License",
         "Operating System :: OS Independent",
     ],
 )