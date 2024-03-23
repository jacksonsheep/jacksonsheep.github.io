---
title: weechat
date: 2024-03-10 15:12:49
tags:
 - tool
---
install step
```
apt install weechat -y
```
1. 连接irc服务端
```
weechat 
/server list        #查看当前可用的服务端信息
/server info freenode     # 查看freenode服务器的详细信息
/server add freenode irc.freenode.cn  # 添加freenode服务器
/connect freenode    # 连接对应服务器
```

2. 进入频道
```
/list       # 查看所有频道
/join #linuxba  #进入linuxba频道
```

3. 用户设置
```
/set
```

4. 帮助文档
```
/help       # 查看可用命令
/connect help     # 查看connect 的帮助文档
```
