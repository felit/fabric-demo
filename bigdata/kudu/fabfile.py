# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
# env.hosts=['vagrant@192.168.18.164']
env.hosts=['root@139.198.6.107']
""" Check failed: _s.ok() Bad status: Not implemented: The CPU on this system (QEMU Virtual CPU)
 does not support the SSE4.2 instruction set which is required for running Kudu.
 If you are running inside a VM, you may need to enable SSE4.2 pass-through.
 """
def install_pre_requirements():
    sudo('yum install -y autoconf automake cyrus-sasl-devel cyrus-sasl-gssapi cyrus-sasl-plain gcc gcc-c++ gdb git krb5-server krb5-workstation libtool make openssl-devel patch pkgconfig redhat-lsb-core rsync unzip vim-common which')
    sudo('yum install -y ntp lsb')
    sudo('chkconfig ntpd on')
    sudo('service ntpd start')

@task
def install():
    with cd('/etc/yum.repos.d'):
        sudo('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/cloudera-kudu.repo')
    sudo('yum install -y kudu kudu-master kudu-tserver kudu-client0 kudu-client-devel')

@task
def install_by_rpm():

    for file in files:
        pass
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-master-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-tserver-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-debuginfo-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-client0-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')
    run('wget http://archive.cloudera.com/kudu/redhat/6/x86_64/kudu/5/RPMS/x86_64/kudu-client-devel-1.3.0+cdh5.11.1+0-1.cdh5.11.1.p0.27.el6.x86_64.rpm')

def config_master():
    sudo('')


def config_tserver():
    sudo('')