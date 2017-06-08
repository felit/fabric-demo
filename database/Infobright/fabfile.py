# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files
"""
Infobright是开源的MySQL数据仓库解决方案，引入了列存储方案，高强度的数据压缩，优化的统计计算(类似sum/avg/group by之类)，
"""