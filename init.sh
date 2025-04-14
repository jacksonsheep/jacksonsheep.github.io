# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

# You may uncomment the following lines if you want `ls' to be colorized:
# export LS_OPTIONS='--color=auto'
# eval "$(dircolors)"
# alias ls='ls $LS_OPTIONS'
# alias ll='ls $LS_OPTIONS -l'
# alias l='ls $LS_OPTIONS -lA'
#
# Some more alias to avoid making mistakes:
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'

alias ls='ls -CF --color'
alias l='ls -CF --color'
alias la='ls -A --color'
alias li='ls -ai --color'
alias ll='ls -alF --color'
alias vi="nano"
alias log='tail -n 400 -f /var/log/syslog'
alias mystat='dstat -cdnmrtg'
alias stop-name='stop-name(){ ps aux|grep $1| grep -v grep |awk '\''{print $2}'\''|xargs kill -15; };stop-name'
alias stop-name-force='stop-force(){ ps aux|grep $1| grep -v grep |awk '\''{print $2}'\''|xargs kill -9; };stop-force'
alias pyvenv='source /root/venv/bin/activate; cd ~/demo/base/python3'
alias redis-cli='redis-cli -a 0706Test --no-auth-warning'
alias sqlite='sqlite3 ~/demo/base/infra.db'
alias weather='curl https://wttr.in/?Jina'
alias doc='/root/demo/base/doc.sh '
alias start-blog='cd /root/demo; npm run server &> /root/demo/server.log &'
alias weechat='cd /root; weechat'
alias psql='docker exec -it postgres psql'
alias mysql='docker exec -it mysql mysql -uroot -p'
alias mutt='cd /root; mutt'
alias todo='nano ~/demo/base/todo.md'
alias init='nano ~/.bashrc'
alias ai='python3 ~/demo/base/python3/ai.py'
alias rmi='mv -t ~/.trash'
alias hosts='curl https://raw.hellogithub.com/hosts >> /etc/hosts'
alias mongo='docker exec -it mongo mongo'
alias space='echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"'
alias bat='bat(){ cat $1 |less; };bat'
# cat ~/demo/base/todo.md
if [ $(mount -l |grep xfs|wc -l) -eq 0 ];then
    sh /opt/xfs.sh
fi
journalctl --vacuum-size=10K
echo "/var/log/core/core.%e.%p.%h.%t" | tee /proc/sys/kernel/core_pattern
export HISTTIMEFORMAT='%F %T '
export WEECHAT_HOME='/opt/weechat'

#export LANG=zh_CN.UTF-8
#export LC_ALL=zh_CN.UTF-8



# evince *.pdf   view pdf file
