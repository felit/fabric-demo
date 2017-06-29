# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files

"""

"""
env.roledefs = {
    'go': ['vagrant@192.168.18.164']
}
env.password = 'vagrant'


@roles('go')
def get_go_files():
    run('wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz')
    run('chown -R vagrant:vagrant /opt')
    run('tar -zxvf go1.8.linux-amd64.tar.gz -C /opt')
    files.append('.bashrc', 'export GOROOT=/opt/go')
    files.append('.bashrc', 'export GOBIN=$GOROOT/bin')
    files.append('.bashrc', 'export GOPKG=$GOROOT/pkg/tool/linux_amd64')
    files.append('.bashrc', 'export GOPKG=amd64')
    files.append('.bashrc', 'export GOOS=linux')
    files.append('.bashrc', 'export GOPATH=$GOROOT')
    files.append('.bashrc', 'export PATH=$PATH:$GOBIN:$GOPKG:$GOPATH/bin')


@roles('go')
def yum_install():
    """
        export GOPATH=/var/www/html
        export PATH=$PATH:$GOPATH/bin
    :return:
    """
    sudo('yum install epel -y')
    sudo('yum install go -y')