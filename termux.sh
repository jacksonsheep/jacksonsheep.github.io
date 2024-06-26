termux-change-repo -r https://mirrors.tuna.tsinghua.edu.cn/termux/stable
#pkg update 

pkg install openssh git nginx w3m man nodejs vim weechat sqlite python -y


ls /data/data/com.termux/files/usr|xargs -i ln -s /data/data/com.termux/files/usr/{} ./{}
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ct %cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global log.date format:"%Y-%m-%d %H:%M:%S"
git clone git@github.com:jacksonsheep/jacksonsheep.github.com -b blog demo
git clone https://gitee.com/zhang-955/clone.git
git clone https://gitee.com/mirrors/ceph.git 
git clone https://gitee.com/mirrors/NFS-Ganesha.git -b V5.7 ganesha
git clone https://gitee.com/mirrors/Linux.git
git clone https://github.com/samba-team/samba

cd demo; npm install; npm install -g hexo-cli;npm run build

#echo -e "#!/bin/bash\nifconfig |grep -A 2 wlan0 |grep inet -w |tr -s '\ '|cut -d ' ' -f 3\nwhoami\n\nalias la='ls -a'\nalias ll='ls -ilF'\nalias vi='nano'\nalias hexo-add='hexo new'\nsshnum=`ps -ef|grep /data/data/com.termux/files/usr/bin/sshd|grep -v grep|wc -l`\necho $sshnum\nif [ $sshnum -eq 0 ];then\n    sshd\nfi" > /data/data/com.termux/files/usr/etc/profile.d/init.sh
cat > /data/data/com.termux/files/usr/etc/profile.d/init.sh << EOF
#!/bin/bash
ifconfig |grep -A 2 wlan0 |grep inet -w |tr -s '\ '|cut -d ' ' -f 3
whoami

alias la='ls -a'
alias ll='ls -ilF'
alias vi='nano'
alias hexo-add='hexo new'
alias weather='curl -0 wttr.in/jinan'
alias doc='sh ~/doc.sh'
export LANG=C.UTF-8
export LC_CTYPTE=C.UTF-8

sshnum=\`ps -ef|grep /data/data/com.termux/files/usr/bin/sshd|grep -v grep|wc -l\`
echo \$sshnum
if [ \$sshnum -eq 0 ];then
    sshd
fi
EOF

chmod +x /data/data/com.termux/files/usr/etc/profile.d/init.sh ~/demo/base/doc.sh
ln -s /storage/emulated/0 ~/storage
ln -s /data/data/com.termux/files/usr/etc/profile.d/init.sh ~/init.sh
ln -s ~/demo/base/doc.sh ~/doc.sh
ln -s ~/demo/base ~/base
ln -s ~/demo/source ~/base/source
ln -s ~/storage/project ~/base/project
