MemAdmin是一款可视化的Memcached管理与监控工具，使用PHP开发，体积小，操作简单。

主要功能：

服务器参数监控：STATS、SETTINGS、ITEMS、SLABS、SIZES实时刷新
服务器性能监控：GET、DELETE、INCR、DECR、CAS等常用操作命中率实时监控
支持数据遍历，方便对存储内容进行监视
支持条件查询，筛选出满足条件的KEY或VALUE
数组、JSON等序列化字符反序列显示
兼容memcache协议的其他服务，如Tokyo Tyrant (遍历功能除外)
支持服务器连接池，多服务器管理切换方便简洁