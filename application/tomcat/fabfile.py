# -*- coding:utf8 -*-
# 安装

from __future__ import with_statement
from fabric.api import run, cd, task, local
import logging


@task
def install(path="~/", user='root', install_path='/opt/tomcat', local_path=None, sudo=False):
    if local_path is not None:
        local('scp %s root@120.78.210.65:%s' % (local_path, path))

    with cd(path):
        print(path)
        tomcat_filename = run("ls -lh | grep tomcat | tail -1 | awk '{print $9}'")

    run('tar -zxvf %s' % tomcat_filename)
    dir = run("tar -tf %s | awk -F/ '{print $1}' | tail -n 1" % tomcat_filename, shell=False)
    run('mv %s %s' % (dir, install_path))


@task
def start(tomcat_root="/opt/tomcat"):
    with cd(tomcat_root):
        run('bin/start.sh')