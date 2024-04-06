function stop_and_clean(){
        systemctl stop docker
        find /var/log/ |grep -E 'gz|1'|xargs rm -rf
        truncate -s 0 /var/log/syslog /var/log/message
        echo 3 >/proc/sys/vm/drop_caches
        echo 'done to stop'
}
        export LANG=C.UTF-8
        export LC_CTYPTE=C.UTF-8
function stack(){
        pid=$1
        ps -T -p ${pid}
        cd /proc/${pid}/task;
        for i in `ls ./`;do
                echo -e "\n"${i}
                cat ./${i}/stack
        done
}
if [ -n "$1" ];then
        key=$1
        echo 'input key:'$key
        case $key in
                'stop') stop_and_clean; exit 0 ;;
                'stack') stack $2; exit 0 ;;
		*) echo 'error inpur param';;
        esac
else
        echo 'empty param input'
fi

