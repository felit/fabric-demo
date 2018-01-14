# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = [
    'vagrant@192.168.18.190',
    'vagrant@192.168.18.191',
    'vagrant@192.168.18.192',
]
env.password = 'vagrant'


@task
def install():
    sudo('apt install -y ipvsadm')
    sudo('apt install -y haproxy')
    sudo('apt install -y nginx')
    sudo('apt install -y keepalived')


@task
@hosts(['vagrant@192.168.18.190'])
def config():
    # sudo('ifconfig eth1:2 192.168.18.189 broadcast 192.168.18.255 netmask 255.255.255.0')
    sudo('echo 1 > /proc/sys/net/ipv4/ip_forward')
    sudo('echo 0 > /proc/sys/net/ipv4/conf/all/send_redirects')
    sudo('echo 0 > /proc/sys/net/ipv4/conf/default/send_redirects')
    sudo('echo 0 > /proc/sys/net/ipv4/conf/eth0/send_redirects')
    sudo('echo 0 > /proc/sys/net/ipv4/conf/eth1/send_redirects')
    sudo('iptables -t nat -F')
    sudo('iptables -t nat -X')
    sudo('iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE')
    sudo('ipvsadm -C')
    sudo('ipvsadm -A -t 192.168.18.190:80 -s wrr')
    # sudo('ipvsadm -a -t 192.168.18.189:80 -r 192.168.18.190:80 -m -w 1')
    sudo('ipvsadm -a -t 192.168.18.190:80 -r 192.168.18.191:80 -m -w 1')
    sudo('ipvsadm -a -t 192.168.18.190:80 -r 192.168.18.192:80 -m -w 1')


@task
@hosts(['vagrant@192.168.18.190'])
def clear_config():
    sudo('ipvsadm -D -t 192.168.18.189:80')


@task
@hosts(['vagrant@192.168.18.190'])
def status():
    sudo('ipvsadm -L -n')