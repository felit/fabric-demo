# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']

"""
TODO 添加认证
tar -zxvf iscsitarget-1.4.20.2.tar.gz
cd iscsitarget-1.4.20.2
sudo yum install -y patch
make
sudo make install
yum install -y  iscsi-initiator-utils


sudo mount  /dev/sdd iscsi-dir
手工发现:
sudo  iscsiadm -m discovery --type sendtargets --portal 192.168.18.166
sudo iscsiadm -m node -T iqn.2001-04.com.example:storage.disk2.sys1.xyz -p 192.168.18.166 --login


sudo iscsiadm -m node -T iqn.2001-04.com.example:storage.disk2.sys1.xyz -p 192.168.18.166 --login


#ietd.conf
Target iqn.2001-04.com.example:storage.disk2.sys1.xyz
Lun 1 Path=/dev/sda1,Type=fileio,ScsiId=xyz,ScsiSN=xyz
"""


@task
@parallel
def install_target():
    """
    # sudo  yum -y install scsi-target-utils
    :return:
    """
    sudo('yum -y install scsi-target-utils')


@task
@parallel
def install_initiator():
    """
    客户端
    :return:
    """
    sudo('yum install -y iscsi-initiator-utils')
