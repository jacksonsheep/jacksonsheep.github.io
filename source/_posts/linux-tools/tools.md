---
title: tool
date: 2022-07-06
tags: 
- tool
- git
---

## git 命令：整体流程，先pull获取最新代码，合并后提交本地，之后push

- git init 初始化git本地仓库
- git log 展示提交日志

  - git log --pretty=oneline 线性展示日志
  - git log --graph	以树形展示日志
- git reflog 展示操作日志
- git reset --soft HEAD^ 返回上次提交
- git rm --cached `<file>`  从暂存区删除文件，但不改变文件区
- git status 当前状态
- git commit -m "note"	提交代码
- git remote 查看远程状态

  - git remote -v 显示详细远程状态
- git push origin [master/dev]	推送分支
- git pull <远程主机名> <远程分支名>:<本地分支名>  拉取分支
- git clone git@github.com:.../.git		从远程克隆项目
- git rebase 变基，将修改前的基础转换为最新状态
- git branch [name]	创建分支

  - git checkout [name] 切换分支
  - git branch	查看分支
  - git merge [name]	合并分支
    - git merge --no-ff -m "merge with no-ff" dev	合并生成新的提交，当分支删除，信息仍然存在
  - git branch -d [name]	删除分支
  - git branch -D [name]	强行删除分支
  - git stash 储存当前分支状态
  - git stash list 查看可回复状态
  - git stash apply 回复+ git shash drop 删除
  - git stash pop 回复并删除
  - git cherry-pick [number] 将master修改的bug复制到当前分支
- git tag 查看所有标签

  - git tag [name] 打开新的标签， 状态为当前状态
  - git tag [name] [number] 提交number对应状态的标签name
  - git show [name]	显示标签内容
  - git tag -d [name]	删除标签
  - git push origin :refs/tags/[name] 删除远程标签

## idea

- 常用函数

  - @deprecated 该类已过时
  - //todo	后期可添加内容
- 常用快捷键

  - http：get,post,delete,put用http Tools调试
  - 相机图标截取当前线程状态 ：查看在运行中的线程
  - 打断点，调试
  - 找到实现 ctrl+点击   或者 前方图标
  - ctrl+shift+/	区块注释
  - Alt+Insert 	产生构造方法、getter/setter等方法
  - Ctrl+R		替换
  - Shift+Enter 	在当前行的下方开始新行
  - Ctrl+Alt+Enter 	在当前行上方插入新行
  - Ctrl + Alt + b 	转到实现
  - Ctrl+Alt+L 	格式化代码
  - ctrl+Q 		查看方法说明
  - Ctrl+D 		复制光标所在行的内容，插入光标位置下面
  - psvn		main
  - sout		默认输出
  - itar		for遍历

## vscode

- ctrl+E    oepn folder explose

## notepad
- ctrl d  复制当前行
- ctrl l  删除当前行

## vim
yy   复制光标当前行
n    粘贴剪切板的行到光标位置

## nano

## linux operate
deb 
  其余文件，安装后覆盖到根目录
  DEBIAN
    control
      Package    程序名称    中间不能有空格
      Version    软件版本     
      Description    程序说明     
      Section    软件类别    utils, net, mail, text, x11
      Priority    软件对于系统的重要程度    required, standard, optional, extra等；
      Essential    是否是系统最基本的软件包    yes/no，若为yes,则不允许卸载（除非强制性卸载）
      Architecture    软件所支持的平台架构    i386, amd64, m68k, sparc, alpha, powerpc等
      Source    软件包的源代码名称     
      Depends    软件所依赖的其他软件包和库文件    若依赖多个软件包和库文件，采用逗号隔开
      Pre-Depends    软件安装前必须安装、
      配置依赖性的软件包和库文件    常用于必须的预运行脚本需求
      Recommends    推荐安装的其他软件包和库文件     
      Suggests    建议安装的其他软件包和库文件 
    postinst(postinstallation)  负责完成安装包时的配置工作。如新安装或升级的软件重启服务。软件安装完后，执行该Shell脚本，一般用来配置软件执行环境，必须以“#!/bin/sh”为首行。
    postrm(postremove)  负责修改软件包链接或文件关联，或删除由它创建的文件。软件卸载后，执行该Shell脚本，一般作为清理收尾工作，必须以“#!/bin/sh”为首行
    preinst(preinstallation)   在Deb包文件解包之前（即软件安装前），将会运行该脚本。可以停止作用于待升级软件包的服务，直到软件包安装或升级完成。
    prerm(preremove) 该脚本负责停止与软件包相关联的daemon服务。它在删除软件包关联文件之前执行。
    copyright(版权)
    changlog(修订记录)
    conffiles

dpkg
  dkpg -b . mydeb.deb  打包
  dkpg -i mydeb.deb    装包（添加 --force-depends 强制安装）
  dpkg --unpack mydeb.deb  解压包，不安装
  dpkg -c mydeb.deb    查看deb包文件内容
  dpkg --info mydeb.deb  查看deb包信息
  dpkg -L mydeb         列出deb包关联的文件
  dpkg -s|--status mydeb         查看deb包是否安装，查看安装信息
  dpkg -r mydeb         卸载deb包，保留配置文件
  dpkg -P|--purge mydeb         删除deb包，删除配置文件
  apt-get install ./mydeb.deb    安装依赖包，安装deb包~
