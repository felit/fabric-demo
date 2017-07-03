# -*- coding:utf8 -*-
"""

"""

from __future__ import with_statement
from fabric.api import run, env, task, parallel, sudo
from fabric.contrib import files

env.hosts = ['vagrant@192.168.18.164', 'vagrant@192.168.18.166']
env.password = 'vagrant'


def install():
    pass


@task
def yum():
    if not files.exists('/etc/yum.repos.d/epel.repo'):
        repo_content = """[epel]
name=epel
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-$releasever&arch=$basearch
enabled=1
gpgcheck=0"""
        files.append('/etc/yum.repos.d/epel.repo', repo_content, use_sudo=True)
        sudo('yum clean all')
        sudo('yum makecache')
    run('sudo yum install -y docker-io')


def kernel():
    sudo('yum upgrade -y device-mapper-libs')


def start_service():
    sudo('service docker start')


def config():
    pass
