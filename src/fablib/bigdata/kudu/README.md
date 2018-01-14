错误:
Log line format: [IWEF]mmdd hh:mm:ss.uuuuuu threadid file:line] msg
F0701 00:49:58.291924  5501 master_main.cc:68] Check failed: _s.ok() Bad status: Service unavailable: Cannot initialize clock: Error reading clock. Cl
ock considered unsynchronized

解决办法: service ntpd start