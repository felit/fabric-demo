# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files


@task
def install():
    sudo('apt-get -y install apache2 libapache2-mod-php5 php5-mysql php5-gd')
