 Fountain是监查、捕捉MySQL数据库的增量变化，分发数据变化给消费者处理的一套解决方案。

    Fountain，英[ˈfaʊntən]，是”源泉“的意思，MySQL数据库源源不断的下发增量，因此而得名。

    任何需要快速、准确接收MySQL数据变化增量的场景均适用，例如

广告传输流：输出到本地增量文件

数据同步：可数据库同构复制，也可以跨异构数据源sync，比如MySQL到一些NoSQL，例如redis、mongodb，或者es、solr等提供搜索服务，或者MQ如bigpipe、RabbitMQ。

缓存失效：数据变化收敛到MySQL，利用增量变化触发memcache或者redis缓存失效。

数据监控：监控数据库中的异常数据，攻击行为数据。

 历史操作记录：数据库业务变化，同步到另外的数据库表，供查询操作记录

 其他你所想到场景...

    Fountain支持MySQL的row base binlog协议，稳定测试版本支持MySQL5.1-5.6。