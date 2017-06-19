TomP2P 是一个基于 P2P 的高性能 key-value 结对数据的存储方案，每个结对数据拥有一个表（基于磁盘或者内存）用来存储其值，单个值可被查询或者更新，底层的通讯框架使用 Java 的 NIO ，支持大量并发连接。

主要特点：


使用 Java5 NIO 实现的分布式哈希表 DHT
XOR-based iterative routing similar to Kademlia.
标准的 DHT 操作：put, get
扩展 DHT 操作，支持自定义操作
Direct and indirect replication.
Mesh-based distributed tracker.
基于签名的数据保护
端口跳转检测以及通过 UPNP 配置
支持 IPv6 和 IPv4
Network operations support the listenable future objects concept.


http://tomp2p.net/doc/