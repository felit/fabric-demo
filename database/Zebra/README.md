Zebra是点评内部使用的数据库访问层中间件，它具有以下的功能点：
    配置集中管理，动态刷新
    支持读写分离、分库分表
    丰富的监控信息在CAT上展现

其中的三个组件的功能分别是：
    zebra-api : 最主要的访问层中间件
    zebra-ds-monitor-client：基于CAT的监控(可选)
    zebra-dao：基于MyBatis的异步化的DAO组件(可选)