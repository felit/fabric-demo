# -*- coding:utf8 -*-
from setuptools import setup, find_packages

setup(
    name="fabric-library",
    version="0.0.2",
    description="library for fabric",
    author="jack.cong",
    author_email='congshuanglong@126.com',
    url="http://blog.livedrof.com",
    license="LGPL",
    packages=find_packages(exclude=['test']),
    scripts=["languages/java/jdk/fabfile.py"],
    py_modules=["languages", "languages.java", "languages.java.jdk", "languages.java.jdk.fabfile",
                "application", "application.tomcat", "application.tomcat.fabfile"]
)
