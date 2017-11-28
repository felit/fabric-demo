# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files


def pre_requirement():
    run('yum install -y openssl openssl-devel lzo lzo-devel pam pam-devel automake pkgconfig')