termux-change-repo -r https://mirrors.tuna.tsinghua.edu.cn/termux/stable
#pkg update 

pkg install openssh git w3m nodejs -y


ls /data/data/com.termux/files/usr|xargs -i ln -s /data/data/com.termux/files/usr/{} ./{}
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

git clone https://gitee.com/yuxuanyang/Gitdemo.git -b blog blog
cd blog; npm install; npm install -g hexo-cli;npm run build

echo -e "#!/bin/bash\nifconfig |grep -A 2 wlan0 |grep inet -w |tr -s '\ '|cut -d ' ' -f 3\nwhoami\n\nalias la='ls -a'\nalias ll='ls -ilF'\nalias vi='nano'\nalias hexo-add='hexo new'\nsshnum=`ps -ef|grep /data/data/com.termux/files/usr/bin/sshd|grep -v grep|wc -l`\necho $sshnum\nif [ $sshnum -eq 0 ];then\n    sshd\nfi" > /data/data/com.termux/files/usr/etc/profile.d/init.sh
