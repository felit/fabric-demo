# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

""" Check failed: _s.ok() Bad status: Not implemented: The CPU on this system (QEMU Virtual CPU)
 does not support the SSE4.2 instruction set which is required for running Kudu.
 If you are running inside a VM, you may need to enable SSE4.2 pass-through.
 """
@task
def install():
    # wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/cloudera-kudu.repo
    # sudo('sudo yum install -y autoconf automake cyrus-sasl-devel cyrus-sasl-gssapi cyrus-sasl-plain gcc gcc-c++ gdb git krb5-server krb5-workstation libtool make openssl-devel patch pkgconfig redhat-lsb-core rsync unzip vim-common which')
    sudo('yum install -y kudu kudu-master kudu-tserver kudu-client0 kudu-client-devel')