# -*- coding:utf8 -*-
from __future__ import with_statement

from fabric.api import run, env, task

from src.fablib.languages.java.jdk import fabfile as jdk


env.hosts = [
    # 'vagrant@192.168.18.166',
    'vagrant@192.168.18.167',
    # 'vagrant@192.168.18.190'
]


def pre_requirement():
    jdk.install('/home/vagrant', local_path='/data/software/jdk-8u66-linux-x64.tar.gz')


@task
def install():
    pre_requirement()
    install_cassandra()

@task
def install_cassandra():
    filename= 'cassandra.tar.gz'
    run('wget http://mirrors.tuna.tsinghua.edu.cn/apache/cassandra/3.11.0/apache-cassandra-3.11.0-bin.tar.gz -O %s'%filename)
    run('tar -zxvf cassandra.tar.gz')
    dirname = run("tar -tf %s | awk -F/ '{print $1}' | tail -n 1" % filename, shell=False)
    run('mv %s /opt/cassandra' % dirname)


def config():
    pass