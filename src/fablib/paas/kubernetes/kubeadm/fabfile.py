# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import sudo, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, local
from fabric.contrib import files
import logging
