---
title: tool
date: 2025-07-16
tags:
- tool
---


## 1. 打开文件浏览器

:Ex[plore]         " 打开当前文件所在目录
:Sex[plore]        " 在水平分割窗口中打开
:Vex[plore]        " 在垂直分割窗口中打开
:Tex[plore]        " 在新标签页中打开
:Ex [目录路径]     " 打开指定目录

## 2. 在文件浏览器中导航
j/k：上下移动光标
h/l 或 Enter：进入 / 退出目录
%：创建新文件
d：创建新目录
D：删除文件或空目录
R：重命名文件或目录
yy：复制文件名（用于后续粘贴操作）
p：在当前目录粘贴文件（需先复制）
r：刷新文件列表

## 3. 快速打开文件
o：在当前窗口打开文件
v：在垂直分割窗口中打开文件
s：在水平分割窗口中打开文件
t：在新标签页中打开文件
## 4. 排序方式
i：切换显示模式（详细列表 / 图标等）
I：显示 / 隐藏隐藏文件（以 . 开头的文件）
q：按名称排序（再次按 q 反转顺序）
t：按修改时间排序
s：按文件大小排序

## 5. 书签功能
ma：将当前目录标记为书签 a（可使用任意字母）
`a：跳转到书签 a 标记的目录



## 6. 自定义配置
在 .vimrc 中添加以下配置可提升 netrw 的使用体验：
vim
" 启用文件图标显示（需要安装 nerd-fonts）
let g:netrw_liststyle = 3

" 隐藏冗余信息
let g:netrw_banner = 0

" 自动切换目录（跟随当前文件）
let g:netrw_keepdir = 0

" 高亮当前文件
let g:netrw_hide=1

" 设置快捷键
nnoremap <leader>e :Ex<CR>        " 快速打开文件浏览器
nnoremap <leader>se :Sex<CR>      " 水平分割打开
nnoremap <leader>ve :Vex<CR>      " 垂直分割打开


四、与当前文件联动
:Lexplore：在左侧垂直分割窗口打开文件浏览器
:Rexplore：在右侧垂直分割窗口打开文件浏览器
:Sexplore：在上方水平分割窗口打开文件浏览器
:Zexplore：打开文件浏览器并折叠其他窗口
五、实用技巧
快速定位当前文件：
在文件浏览器中按 %，自动定位到当前编辑的文件。
浏览远程文件：
vim
:e scp://用户名@服务器地址/路径/   " 通过 SSH 浏览远程文件

FTP 功能：
vim
:e ftp://用户名:密码@服务器地址/路径/

六、退出文件浏览器
:q：关闭当前文件浏览器窗口
:only：关闭其他所有窗口，只保留当前窗口
七、常见问题
中文乱码：
在 .vimrc 中添加：
vim
set fileencodings=utf-8,gbk,ucs-bom,cp936

性能优化：
vim
let g:netrw_localcopydircmd = "cp -r"  " 加速复制大目录
let g:netrw_async = 1                  " 启用异步操作
