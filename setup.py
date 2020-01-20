"""Setup file
"""

import setuptools

import dagtools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='gravtools',
                 version=dagtools.__version__,
                 description='Tools for manipulating Directed Acyclic Graphs in Python',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url=dagtools.__github_url__,
                 author='James W. Kennington',
                 author_email='jameswkennington@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 zip_safe=False)
