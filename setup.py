# -*- coding:utf8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

long_description = """
/data/source/self/fabric-demo/reinstall.sh/data/source/self/fabric-demo/reinstall.sh
----
%s
----

""" % (readme)

setup(
    name="fablib",
    version="0.0.3",
    description="library for fabric",
    long_description=long_description,
    author="jack.cong",
    author_email='congshuanglong@126.com',
    # url="http://blog.livedrof.com",
    url="http://fablib.livedrof.com",
    license="LGPL",
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
