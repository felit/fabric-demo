# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, local
from fabric.contrib import files

env.hosts = ['root@139.198.6.107', 'root@www.livedrof.com']
env.roledefs = {
    'mysql': 'root@139.198.6.107'
}
global_var = 900


def get_hosts():
    print global_var
    print env.roles
    print [0,1,2,3,4][1:]