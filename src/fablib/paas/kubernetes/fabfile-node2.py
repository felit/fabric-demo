# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, local
from fabric.contrib import files
import logging

env.hosts = [
    'vagrant@192.168.18.192'
]
env.password = "vagrant"

"""
centos7
"""
# 10.62.102.114
@task
def install():
    # sudo('yum update')
    # sudo('yum makecache')
    # sudo('yum install -y etcd kubernetes ntp flannel')
    # sudo('systemctl disable firewalld')
    # sudo('systemctl stop firewalld')
    # sudo('ntpdate ntp1.aliyun.com')
    # sudo('hwclock -w')
    # sudo('hostname k8s-node-2')
    # sudo('echo k8s-node-2 > /etc/hostname')
    # TODO 这里有问题Error
    if files.exists('/etc/sysconfig/flanneld'):
        sudo('rm /etc/sysconfig/flanneld')
    print files.append("/etc/sysconfig/flanneld", """
FLANNEL_ETCD_ENDPOINTS="http://192.168.18.190:2379"
FLANNEL_ETCD_PREFIX="/k8s/network"
FLANNEL_OPTIONS="--iface=eth0"
    """,use_sudo=True)

    if files.exists('/etc/kubernetes/config'):
        sudo('rm /etc/kubernetes/config')
    files.append('/etc/kubernetes/config', """
KUBE_LOGTOSTDERR="--logtostderr=true"
KUBE_LOG_LEVEL="--v=0"
KUBE_ALLOW_PRIV="--allow-privileged=false"
KUBE_MASTER="--master=http://192.168.18.190:8080"
    """,use_sudo=True)

    if files.exists('/etc/kubernetes/proxy'):
        sudo('rm /etc/kubernetes/proxy')
    files.append('/etc/kubernetes/proxy', """
KUBE_PROXY_ARGS="--bind-address=0.0.0.0"
    """,use_sudo=True)

    if files.exists('/etc/kubernetes/kubelet'):
        sudo('rm /etc/kubernetes/kubelet')
    files.append('/etc/kubernetes/kubelet', """
KUBELET_ADDRESS="--address=127.0.0.1"
KUBELET_HOSTNAME="--hostname-override=k8s-node-2"
KUBELET_API_SERVER="--api-servers=http://192.168.18.190:8080"
KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=registry.access.redhat.com/rhel7/pod-infrastructure:latest"
KUBELET_ARGS=""
    """,use_sudo=True)


@task
def start():
    sudo("""
for SERVICES in flanneld kube-proxy kubelet; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES
done
    """)


@task
def status():
    sudo('kubectl version')
    sudo('kubectl get nodes')


@task
def config_ssh():
    # sudo('mkdir .ssh')
    sudo('chmod 700 .ssh')
    # sudo('touch .ssh/authorized_keys')
    sudo('chmod 600 .ssh/authorized_keys')
    files.append('.ssh/authorized_keys', """
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl
    """)