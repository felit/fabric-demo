
# git clone https://github.com/alibaba/canal.git
# cd canal;
# mvn clean install -Dmaven.test.skip -Denv=release

#[mysqld]
# log-bin=mysql-bin #添加这一行就ok
# binlog-format=ROW #选择row模式
# server_id=1 #配置mysql replaction需要定义，不能和canal的slaveId重复

# CREATE USER canal IDENTIFIED BY 'canal';
# GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal'@'%';
# -- GRANT ALL PRIVILEGES ON *.* TO 'canal'@'%' ;
# FLUSH PRIVILEGES;


# 配置canal
# canal.instance.mysql.slaveId = 1234
# canal.instance.master.address = 127.0.0.1:3306
# canal.instance.master.journal.name =
# canal.instance.master.position =
# canal.instance.master.timestamp =
#
# canal.instance.dbUsername = canal
# canal.instance.dbPassword = canal
# canal.instance.defaultDatabaseName =
# canal.instance.connectionCharset = UTF-8
#
# canal.instance.filter.regex = .\..

# 启动canal
# bin/startup.sh