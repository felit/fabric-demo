# -*- coding:utf8 -*-
# 安装
"""

"""

from __future__ import with_statement
from fabric.api import run, env, task
from fabric.contrib import files

env.hosts = [
    # 'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
    'root@www.livedrof.com'
]


def test_install():
    install()


@task
def install(url='https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz'):
    run('wget %s -O go.tar.gz' % url)
    run('tar -zxvf go.tar.gz')
    dir = run("tar -tf go.tar.gz | awk -F/ '{print $1}' | tail -n 1",shell=False)
    run('mv %s /opt/' % dir)
    files.append('.bashrc', 'export GOROOT=/opt/go')
    files.append('.bashrc', 'export GOBIN=$GOROOT/bin')
    files.append('.bashrc', 'export GOPKG=$GOROOT/pkg/tool/linux_amd64')
    files.append('.bashrc', 'export GOARCH=amd64')
    files.append('.bashrc', 'export GOOS=linux')
    files.append('.bashrc', 'export GOPATH=$GOROOT')
    files.append('.bashrc', 'export PATH=$PATH:$GOBIN:$GOPKG:$GOPATH/bin')