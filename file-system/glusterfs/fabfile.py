# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']


@task
# @parallel
def install_gluster():
    """
        sudo yum install -y rpcbind nfs-utils
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-libs-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-libs-3.5.9-1.el6.x86_64.rpm
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-3.5.9-1.el6.x86_64.rpm
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-fuse-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-fuse-3.5.9-1.el6.x86_64.rpm
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-api-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-api-3.5.9-1.el6.x86_64.rpm
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-cli-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-cli-3.5.9-1.el6.x86_64.rpm
        wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-server-3.5.9-1.el6.x86_64.rpm
        sudo rpm -ivh glusterfs-server-3.5.9-1.el6.x86_64.rpm
    :return:
    """
    # sudo('yum install -y rpcbind nfs-utils')
    # run('wget https://download.gluster.org/pub/gluster/glusterfs/repos/YUM/glusterfs-3.5/LATEST/CentOS/epel-6.5/x86_64/glusterfs-libs-3.5.9-1.el6.x86_64.rpm')
    # sudo('rpm -ivh glusterfs-libs-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-libs-3.5.9-1.el6.x86_64.rpm')
    run('yum')


def create_volume():
    run('gluster volume create gv0 replica 2 192.168.181.21:/data/gfsdata 192.168.181.22:/data/gfsdata')
    pass


@task
def mkdir_gfs():
    run('mkdir -p /data/gfsdata')


def mount():
    sudo('mkdir /gfs')
    sudo('mount -t glusterfs 192.168.181.21:/gv0 /gfs')
    files.append('192.168.181.21:/data/gfsdata      /mnt/glusterfs    glusterfs  defaults        0 0','/etc/fstab')


@task
def service_gfs():
    """
    设置gfs
    :return:
    """
    sudo('service glusterd start')
    sudo('chkconfig glusterd on')