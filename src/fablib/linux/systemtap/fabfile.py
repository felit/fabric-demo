# wget http://debuginfo.centos.org/6/x86_64/kernel-debuginfo-common-x86_64-`uname -r`.rpm
# wget http://debuginfo.centos.org/6/x86_64/kernel-debuginfo-common-x86_64-2.6.32-696.10.2.el6.x86_64.rpm
# wget http://debuginfo.centos.org/6/x86_64/kernel-debuginfo-2.6.32-696.10.2.el6.x86_64.rpm
# wget http://debuginfo.centos.org/6/x86_64/kernel-debuginfo-`uname -r`.rpm
# yum install kernel-devel kernel-headers kernel
# yum install systemtap systemtap-runtime



# ubuntu
# sudo apt-get install systemtap
# sudo apt-get install systemtap-sdt-dev
# sudo apt-get install dpkg-dev debhelper gawk
# sudo apt-get build-dep --no-install-recommends linux-image-$(uname -r)
# apt-get source linux-image-$(uname -r)
# cd linux-*
# fakeroot debian/rules clean
# AUTOBUILD=1 fakeroot debian/rules binary-generic skipdbg=false
# sudo dpkg -i