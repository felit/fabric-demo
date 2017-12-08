# -*- coding:utf8 -*-
from setuptools import setup, find_packages

setup(
    name="fabric_library",
    version="0.0.2",
    description="library for fabric",
    author="jack.cong",
    author_email='congshuanglong@126.com',
    url="http://blog.livedrof.com",
    license="LGPL",
    packages=find_packages(exclude=['test']),
    scripts=[],
    py_modules=["fabric_library","languages.java.jdk.fabfile"]
)
