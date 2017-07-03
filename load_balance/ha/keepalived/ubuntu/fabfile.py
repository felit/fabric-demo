# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = [
    'vagrant@192.168.18.190',
    'vagrant@192.168.18.191',
    'vagrant@192.168.18.192'
]


@task
def install():
    sudo('apt-get -y install libssl-dev openssl libpopt-dev')


def config_selinux():
    sudo('setenforce 0')
    files.sed('/etc/sysconfig/selinux', 'SELINUX=.*', 'SELINUX=disabled')


def config_iptables():
    sudo('iptables -A INPUT -d 224.0.0.18 -j ACCEPT')