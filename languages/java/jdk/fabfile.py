# -*- coding:utf8 -*-
# 安装
"""
TODO 查找文件
解压文件

"""

from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, local
from fabric.contrib import files
import logging

env.hosts = [
    # 'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
]


@task
def test_install():
    install('/home/vagrant')


@task
def install(path="~/", user='root', install_path='/opt/jdk', local_path=None, sudo=False):
    # 查看根目录d
    # 取第一个
    """
        TODO 如果查不到文件本地上传
        TODO 判断/opt/jdk是否存在,如果存直接删除或提示
        :param path:
        :param install_path:
        :return:
    """
    # 得当前执行的IP等信息
    if local_path is not None:
        local('scp %s %s@%s:%s' % (local_path, env.user, env.host, path))

    with cd(path):
        print(path)
        jdk_filename = run("ls -lh | grep jdk | tail -1 | awk '{print $9}'")

    # print('mkdir -p %s' % install_path)
    # sudo('mkdir -p %s' % install_path)
    # sudo('chown -R vagrant:vagrant /opt')
    run('tar -zxvf %s' % jdk_filename)
    dir = run("tar -tf %s | awk -F/ '{print $1}' | tail -n 1" % jdk_filename, shell=False)
    run('mv %s %s' % (dir, install_path))
    files.append('.bashrc', 'export JAVA_HOME=%s' % install_path)
    files.append('.bashrc', 'export PATH=$JAVA_HOME/bin:$PATH')