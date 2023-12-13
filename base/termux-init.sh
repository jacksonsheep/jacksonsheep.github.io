pkg install python2 git -y 
pkg install x11 proot proot-distro -y
proot-distro install alpine
git clone https://gitee.com/zhang-955/clone.git
cd clone/AutoInstallKali; chmod +x kalinethunter; ./kalinethunter

# init.sh  ~/etc/profile.d/init.sh
echo "ifconfig |grep -A 2 wlan0 |grep inet -w |tr -s '\ '|cut -d ' ' -f 3 \n\
whoami \n\
alias la='ls -a --color ' \n\
alias ll='ls ilF --color' \n\
alial=ls' \n\
al-s 'ias vi='nano' \n\
alias hexo-add='hexo new' \n\
alias github='w3m github.com' \n\
sshd" > /data/data/com.termux/files/usr/etc/profile.d/init.sh
ln -s /data/data/com.termux/files/usr/etc/profile.d/init.sh ~/init.sh
ls /data/data/com.termux/files/usr/ |xargs -i ln -s /data/data/com.termux/files/usr/{} ~/{}
