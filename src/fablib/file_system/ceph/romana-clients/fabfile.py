# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files


@task
@parallel
def install():
    pass