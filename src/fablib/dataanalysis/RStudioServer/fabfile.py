# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
"""
    https://www.rstudio.com/products/rstudio/download-server/
"""

def get_rstudio_server(local_file=None):
    # install R
    # 待定 sudo yum install -y libcrypto.so.6 libgfortran.so.1 libssl.so.6 openssl098e-0.9.8e  gcc41-libgfortran-4.1.2 pango-1.28.1
    # /data/software/rstudio-server-rhel-1.0.143-x86_64.rpm
    if local_file is not None:
        run('scp %s ')
    else:
        run('wget https://download2.rstudio.org/rstudio-server-rhel-1.0.143-x86_64.rpm -O rstudio-server.rpm')
        sudo('rpm -ivh rstudio-server.rpm')


def start_server():
    sudo('rstudio-server start')