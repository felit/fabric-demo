# -*- coding:utf8 -*-
# 安装

from __future__ import with_statement
from fabric.api import run, cd, task, local, env
from fabric.operations import put
from fabric.colors import green
import logging

env.hosts = []

@task
def install(path="~/", user='root', install_path='/opt/tomcat/webapps', local_path=None, sudo=False):
    if local_path is not None:
        put(local_path, install_path)
        print(green("jenkins安装完成,将%s安装至%s" % (local_path, install_path)))
    else:
        run("wget http://updates.jenkins-ci.org/download/war/2.89.1/jenkins.war %s" % install_path)
    # if input(red('{} (y/n) '.format(msg))) != 'y':
    # with cd(path):
    #     print(path)
    #     tomcat_filename = run("ls -lh | grep tomcat | tail -1 | awk '{print $9}'")
    #
    # run('tar -zxvf %s' % tomcat_filename)
    # dir = run("tar -tf %s | awk -F/ '{print $1}' | tail -n 1" % tomcat_filename, shell=False)
    # run('mv %s %s' % (dir, install_path))
