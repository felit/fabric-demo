# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, local
from fabric.contrib import files
import logging

env.hosts = [
    'root@121.201.29.124'
]
env.password = "Rootadmin1"

"""
centos7
"""
# 10.62.102.114
@task
def install():
    run('yum update')
    run('yum makecache')
    run('yum install -y etcd kubernetes ntp flannel')
    run('systemctl disable firewalld')
    run('systemctl stop firewalld')
    run('ntpdate ntp1.aliyun.com')
    run('hwclock -w')
    run('hostname k8s-node-1')
    run('echo k8s-node-1 > /etc/hostname')
    # TODO 这里有问题Error
    files.append("/etc/sysconfig/flanneld", """
FLANNEL_ETCD_ENDPOINTS="http://10.62.98.39:2379"
FLANNEL_ETCD_PREFIX="/k8s/network"
FLANNEL_OPTIONS="--iface=eth0"
    """)

    files.append('/etc/kubernetes/config', """
KUBE_LOGTOSTDERR="--logtostderr=true"
KUBE_LOG_LEVEL="--v=0"
KUBE_ALLOW_PRIV="--allow-privileged=false"
KUBE_MASTER="--master=http://10.62.98.39:8080"
    """)

    files.append('/etc/kubernetes/proxy', """
KUBE_PROXY_ARGS="--bind=address=0.0.0.0"
    """)
    files.append('/etc/kubernetes/kubelet', """
KUBELET_ADDRESS="--address=127.0.0.1"
KUBELET_HOSTNAME="--hostname-override=k8s-node-1"
KUBELET_API_SERVER="--api-servers=http://10.62.98.39:8080"
KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=registry.access.redhat.com/rhel7/pod-infrastructure:latest"
KUBELET_ARGS=""
    """)


@task
def start():
    run("""
for SERVICES in flanneld kube-proxy kubelet; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES
done
    """)


@task
def status():
    run('kubectl version')
    run('kubectl get nodes')


@task
def config_ssh():
    run('mkdir .ssh')
    run('chmod 700 .ssh')
    run('touch .ssh/authorized_keys')
    run('chmod 600 .ssh/authorized_keys')
    files.append('.ssh/authorized_keys', """
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl
    """)