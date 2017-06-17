# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files
"""
Lepus（天兔） 是数据库企业监控系统，针对互联网企业开发的一款专业、强大的企业数据库监控管理系统，企业通过Lepus可以对数据库的实时健康和各种性能指标进行全方位的监控。目前已经支持MySQL、Oracle、MongoDB、Redis数据库的全面监控
"""