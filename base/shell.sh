#!/bin/bash

function do_test(){
	echo 'hello world'
}
function do_ll(){
	if [ ! -d ~/test ]; then
		echo 'mkdir ~/test'
		mkdir ~/test
	fi
	if [ ! -f ~/test/file ]; then
		echo 'touch ~/test/file'
		touch ~/test/file
	fi
	ls -ailF --color  ~/test
}
function killalll(){
	ps aux|grep $1|grep -v grep|awk '{print $2}'|xargs kill -15
	count = ps aux|grep $1|grep -v grep |wc -l
	if [ $count -gt 1 ]; then
		echo "kill -15 fail, then try to kill -9"
		ps aux|grep $1|grep -v grep|awk '{print $2}'|xargs kill -9
	fi
}
function loop(){
	if [ ${#msg[@]} != $1 ];then
		return;
    fi
	msg=$2
	for i in {0..$1};do
		echo ${msg[i]} 
		echo "array lengh= ${#msg[@]} and item length ${#msg[i]}"
	done;
}
function array(){
	declare -A site=(["google"]="www.google.com" ["runoob"]="www.runoob.com" ["taobao"]="www.taobao.com")
	echo "array = ${site[*]} , array key= ${!site[*]}, array length= ${#site[*]}"
}
function read(){
	echo 'input number at below,enter -1 to exit'
	read num;
	echo "read $num"
}
case $1 in
   -1) echo 'test done';break;;
    1) do_test;;
   	2) do_ll;;
    3) killall $2;;
    4) loop $2 $3 ;;
    5) array ;;
    6) read ;;
	*) echo 'error input number';;
esac
