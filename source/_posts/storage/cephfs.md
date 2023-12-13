---
title: cephfs
date: 2022-07-06
tags:
- storage
- ceph
- client
---


# ceph 文件存储总结

## 组织结构
1. Monitor ceph 管理节点，保存并维护各个map信息和权限，日志等集群管理内容
2. MDS  元数据服务器，创建，修改，重命名，删除文件，文件夹等服务的提供者，同时包含挂载和卸载部分。
   1. MDSDaemon mds守护进程，mds创建时通过它来引导其他部分的启动和正常执行内容
   2. MDSRank/MDRankDispatcher, mds的主要消息分发器，和Monitor等集群通信的通过Beacon分发器使用Monc传递消息
   3. Server,  重点业务执行部分，元数据的处理大多位于此
   4. MDCache。 mds缓存处理，对业务快速响应的支持
   5. MDLog， mds日志操作，每个元数据操作先写入日志，确保数据不丢失之后通过日志下刷落盘持久化。
3. OSD  实际存储组件，存储数据和元数据的磁盘管理，底层数据存储原理位于此
   1. rados 一个文件对应多个对象，一个文件夹默认对应一个对象，默认对象大小为4M，超出部分存入下一个对象
   2. pg， 每个对象对应一个pg，映射关系通过hash完成
   3. osd， 每个pg对应多个osd，映射关系为crush算法。osd直接控制每个对象的数据块存储在磁盘的位置，以及日志的存储等内容。


## 源码分析

### mkdir
1. Server--handle_client_mkdir()
   1. 获取或创建当前父级目录的信息，并创建Dentry和父级目录的Dir相连接
   2. 创建空Inode，并和Dentry连接，放入projected队列中
   3. 创建或查找对应dir，并和inode连接
   4. early replay
   5. 写入日志，EUpdate
   6. 回复客户端，并将inode移出projected队列

### ceph-fuse
1. client 向 Monitor 权限认证并订阅monmap，fsmap，osdmap
2. client 向 mds 发送挂载申请，并获取挂载目录 的inode信息
3. client 内核操作，将inode信息更新到vfs中，方便后续使用

### mds 状态切换
1. 
