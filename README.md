1.使用已经存在daemon技术，如init、supervisord、upstart、systemd等，例如：/etc/init.d/tomcat restart 这样的命令，另外supervisord我也是很喜欢的。
2.使用screen、tmux、dtach等工具来从当前shell中detach进程。如：screen -d -m sleep 10 这样的命令。注：要设置pty=False，如 run(‘screen -d -m sleep 10′, pty=False)。
3.使用nohup，不过确实如官方文档所说只有部分用户能成功，我用nohup在run()中时就遇到了问题后该用screen了。
TODO
１、搭建yum与apt本地源，及rsync官方同步及vpn　以加快布署速度