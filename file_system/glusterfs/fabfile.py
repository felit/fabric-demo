# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = ['root@192.168.0.2',
             'root@192.168.0.3',
             'root@192.168.0.4',
             'root@192.168.0.5']


@task
@parallel
@hosts(['root@192.168.0.4'])
def install_gluster():
    prefix = 'https://download.gluster.org/pub/gluster/glusterfs/3.5/LATEST/CentOS/epel-6.5/x86_64/'

    sudo('yum install -y wget rpcbind nfs-utils libaio liblvm2app lvm2-devel')
    run('wget {prefix}/glusterfs-libs-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-libs-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-libs-3.5.9-1.el6.x86_64.rpm')

    run('wget {prefix}/glusterfs-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-3.5.9-1.el6.x86_64.rpm')

    run('wget {prefix}/glusterfs-fuse-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-fuse-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-fuse-3.5.9-1.el6.x86_64.rpm')

    run('wget {prefix}/glusterfs-api-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-api-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-api-3.5.9-1.el6.x86_64.rpm')

    run('wget {prefix}/glusterfs-cli-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-cli-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-cli-3.5.9-1.el6.x86_64.rpm')

    run('wget {prefix}/glusterfs-server-3.5.9-1.el6.x86_64.rpm'.format(prefix=prefix))
    sudo('rpm -ivh glusterfs-server-3.5.9-1.el6.x86_64.rpm')
    run('rm glusterfs-server-3.5.9-1.el6.x86_64.rpm')


def create_volume():
    # gluster peer probe 192.168.0.3
    # gluster volume start gv0
    run('gluster volume create gv0 replica 2 192.168.0.3:/gfsdata 192.168.0.4:/gfsdata')


@task
def mkdir_gfs():
    run('rmdir /data/gfsdata')
    run('mkdir -p /gfsdata')


def mount():
    sudo('mkdir /gfs')
    sudo('mount -t glusterfs 192.168.0.2:/gv0 /gfs')
    files.append('192.168.181.21:/data/gfsdata  /mnt/glusterfs    glusterfs  defaults        0 0', '/etc/fstab')


@task
def status():
    """
       查看状态
    :return:
    """
    sudo('service glusterd status')
    sudo('ls -lh /gfsdata')


@task
def start():
    """
     启动gluster file system
    :return:
    """
    sudo('service glusterd start')
    sudo('chkconfig glusterd on')


@task
@parallel
def stop():
    """
    关闭glusterfs
    :return:
    """
    sudo('service glusterd stop')