MySQL Sniffer 是一个基于 MySQL 协议的抓包工具，实时抓取 MySQLServer 端的请求，并格式化输出。输出内容包括访问时间、访问用户、来源 IP、访问 Database、命令耗时、返回数据行数、执行语句等。有批量抓取多个端口，后台运行，日志分割等多种使用方式，操作便捷，输出友好。

同时也适用抓取 Atlas 端的请求，Atlas 是奇虎开源的一款基于 MySQL 协议的数据中间层项目。

同类型工具还有vc-mysql-sniffer，以及 tshark 的 -e mysql.query 参数来解析 MySQL 协议。

MySQL Sniffer 由奇虎 DBA 和基础设施团队开发。