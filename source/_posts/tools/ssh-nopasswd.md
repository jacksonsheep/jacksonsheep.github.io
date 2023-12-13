---
title: ssh-nopasswd
date: 2023-01-07 09:19:47
tags:
- tool
- ssh
---
1. ssh 客户端端执行 ssh-keygen  生成公钥和私钥到~/.ssh
   > 具体文件为 ~/.ssh/id_rsa(私钥)  ~/.ssh/id_rsa.pub（公钥）
2. ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.235.22 上传公钥到ssh服务器，指定服务器ip和ssh用户名
3. ssh root@192.168.235.22 执行免密登陆
