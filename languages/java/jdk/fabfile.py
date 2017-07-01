# -*- coding:utf8 -*-
# 安装
"""
TODO 查找文件
解压文件

"""

from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings
from fabric.contrib import files

env.hosts = [
    # 'vagrant@192.168.18.164',
    'vagrant@192.168.18.190'
]


@task
def test_install():
    install('/home/vagrant')


@task
def install(path, install_path='/opt/jdk'):
    # 查看根目录d
    # 取第一个
    """
    TODO 如果查不到文件本地上传
        :param path:
        :param install_path:
        :return:
    """
    with cd(path):
        jdk_filename = run("ls -lh | grep jdk | tail -1 | awk '{print $9}'")
    run('tar -zxvf %s' % jdk_filename)
    dir = run("tar -tf %s | awk -F/ '{print $1}' | tail -n 1" % jdk_filename)
    run('mv %s %s' % (dir, install_path))
    files.append('.bashrc', 'export JAVA_HOME=%s' % install_path)
    files.append('.bashrc', 'export PATH=$JAVA_HOME/bin:$PATH')