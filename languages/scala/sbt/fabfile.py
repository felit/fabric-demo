# -*- coding:utf8 -*-
"""

"""

from __future__ import with_statement
from fabric.api import run, env, task, parallel, sudo
from fabric.contrib import files
from common.linux import fabfile as linux

env.hosts = [
    # 'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
    'root@www.livedrof.com'
]

def install():
    if linux.is_centos():
        run('curl https://bintray.com/sbt/rpm/rpm > bintray-sbt-rpm.repo')
        sudo('mv bintray-sbt-rpm.repo /etc/yum.repos.d/')
        sudo('yum install sbt')
    elif linux.is_ubuntu():
        run('echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list')
        sudo('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823')
        sudo('apt-get update')
        sudo('apt-get install sbt')