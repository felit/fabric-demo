rcus 是一个基于 memcached 的云缓存，由 NAVER Corp 公司开发。 arcus-memcached 经过大幅度的修改，可以支持 NAVER 的功能和性能要求。Arcus 支持多种数据机构 (List, Set, B+tree)，除了支持基本的memcached 键值数据模型，还可以一个结构化的形式存储和回取多个数值。

Arcus 管理多个使用 ZooKeeper 的 memcached 节点集群。每个集群或云由它的服务代码标识，以服务代码作为云的名字。用户可以添加／删除 memcached 的 nodes/clouds。Arcus 会检测出失败的 nodes 并自动删除它们。