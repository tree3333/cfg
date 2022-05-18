#!/bin/sh
if [ ! -f ~/hostat/hostat.conf ] ; then
    echo "Can NOT find file ~/hostat/hostat.conf, make it"
    if [ ! -d ~/hostat ] ; then
        mkdir ~/hostat 
    fi 
    touch ~/hostat/records
    touch ~/hostat/ip_records
    cat > ~/hostat/hostat.conf<<EOF
#不要有空格
router=192.168.10.3
username=admin
password=password
#https://sct.ftqq.com获取你自己的key
serverchan_sckey=SCTKEY
#写路由器内网IP地址前3段
sub_net=192.168.10
#写需要监控的IP地址最后一段。用,分割
mon_ip_list=50,51,52,53,10
#检查状态间隔时间，单位为分
sleep_time=5
use_crontab=0
EOF
    exit 1
fi
get_para() {
    [ ! "$3" ] && return
    result=`echo $2 | grep -o "$1$3" | sed "s/$1//"`
    echo $result
}
bytes_for_humans() {
    [ ! "$1" ] && return
    #[ "$1" -gt 1099511627776 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1099511627776'}'`T" && return
    #[ "$1" -gt 1073741824 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1073741824'}'`G" && return
    #[ "$1" -gt 1048576 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1048576'}'` M" && return
    #[ "$1" -gt 1024 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1024'}'` K" && return
    [ "$1" -gt 1000000000000 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000000000000'}'`T" && return
    [ "$1" -gt 1000000000 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000000000'}'`G" && return
    [ "$1" -gt 1000000 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000000'}'` M" && return
    [ "$1" -gt 1000 ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000'}'` K" && return
    echo "${1} bytes"
}
## init Paras
hostat_init(){
    config=`cat ~/hostat/hostat.conf `
    router=`get_para "router=" "$config" "[a-zA-Z0-9.]\+"`
    password=`get_para "password=" "$config" "[a-zA-Z0-9.;:,~!@#$%^&*]\+"`
    username=`get_para "username=" "$config" "[a-zA-Z0-9]\+"`
    sckey=`get_para "serverchan_sckey=" "$config" "[a-zA-Z0-9=/]\+"`
    sub_net=`get_para "sub_net=" "$config" "[0-9.]\+"`
    ip_list=`get_para "mon_ip_list=" "$config" "[0-9,]\+"`
    sleep_time=`get_para "sleep_time=" "$config" "[0-9]\+"`
    use_crontab=`get_para "use_crontab=" "$config" "[0-9]\+"`
    linefeed="%0D%0A"
    markdown_linefeed="%0D%0A%0D%0A"
}

get_stat() {
    ###have cookies
    if [ -f ~/hostat/cookies ]; then
        ##get host status
        #sys_auth=`cat ~/hostat/cookies | grep -o "\w\{32\}"`
        resp=`curl -s -b ~/hostat/cookies "http://${router}/ajax/status/hoststat" | sed 's/"//g'`
        len_of_resp=`echo $resp | wc -c`
        if [ $len_of_resp -lt 10 ];then ### cookies expire
            #echo "cookies expire login"
            resp=`curl -s -c ~/hostat/cookies "http://${router}/cgi-bin/webui/admin" -d "userName=${username}&password=${password}&timestamp=1652511838&csrftoken=MTY1MjUxMTgzOEdPQ0xPVUQ%3D&newwebui=yes&username=admin&type=account"`
            resp=`curl -s -b ~/hostat/cookies "http://${router}/ajax/status/hoststat" | sed 's/"//g'`
        fi
    ### have no cookies
    else
        ##
        #echo "no cookies login"
        resp=`curl -s -c ~/hostat/cookies "http://${router}/cgi-bin/webui/admin" -d "userName=${username}&password=${password}&timestamp=1652511838&csrftoken=MTY1MjUxMTgzOEdPQ0xPVUQ%3D&newwebui=yes&username=admin&type=account"`
        resp=`curl -s -b ~/hostat/cookies "http://${router}/ajax/status/hoststat" | sed 's/"//g'`
    fi
}
check_stat() {
    msg=""
    off_host_num=0
    for ip in `echo $ip_list | sed "s/,/ /g"`;
    do
        ip_addr="${sub_net}.${ip}"
        result=`echo $resp | grep -o "hostname[^{]\+${ip_addr},[^}]\+down_bytes:[0-9.]\+[MGTP]"`
        if [ ! $? -eq 0 ];then
            #host is offline
	    off_host_num=$(($off_host_num+1))
	    msg=$msg"${off_host_num}) IP:${ip_addr}${linefeed}"
	    #msg=$msg"IP:$ip_addr is offline"
        fi
    done
    if [ $off_host_num -gt 0 ];then
        title="您有【${off_host_num}】台设备离线"
        curl -k -s -X POST "http://sc.ftqq.com/${sckey}.send?text=${title}&" -d "desp=${msg}" > /dev/null
    fi
}
check_wanip(){
    if [ -f ~/hostat/ip_records ];then
        saved_ip=`cat ~/hostat/ip_records`
    fi
    if_sts=`ifconfig | sed "s/$/br/g"`
    if_sts=`echo $if_sts | grep -o "pppoe-[^ ]\+ Link encap:Point-to-Point Protocol br inet addr:[0-9.]\+" | awk '{print $1 $7}'` 
    ips=`echo $if_sts | sed "s/pppoe-//g" | sed "s/addr:/ /g"`
    echo $ips > ~/hostat/ip_records
    if [ ! "${ips}"x = "${saved_ip}"x ]; then
        title="IP Changed"
        msg="New:${markdown_linefeed}${ips}${markdown_linefeed}Old:${markdown_linefeed}${saved_ip}"
        curl -k -s -X POST "http://sc.ftqq.com/${sckey}.send?text=${title}&" -d "desp=${msg}" > /dev/null
    fi
    #space_num=`echo $ips | tr -cd " " | wc -c`
    #wan_num=$((($space_num+1)/2))
}
loop() {
    hostat_init
    sleeptime=$(($sleep_time*60))
    while :
    do
        get_stat
        check_stat
        check_wanip
	if [ $use_crontab -eq 0 ]; then
            sleep $sleeptime
	else
            break
	fi
    done
}
unitG(){
    [ "$2" = "G" ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'}'`" && return
    [ "$2" = "T" ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'*'1000'}'`" && return
    [ "$2" = "P" ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'*'1000000'}'`" && return
    [ "$2" = "M" ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000'}'`" && return
    [ "$2" = "K" ] && echo "`awk 'BEGIN{printf "%.2f\n",'$1'/'1000000'}'`" && return
    echo "$1"
}
calc_bytes() {
    byte1=`echo $1 | grep -o "[0-9.]\+"`
    unit1=`echo $1 | grep -o "[MGTPK]"`
    byte2=`echo $2 | grep -o "[0-9.]\+"`
    unit2=`echo $2 | grep -o "[MGTPK]"`
    byte1=`unitG $byte1 $unit1`
    byte2=`unitG $byte2 $unit2`
    b=`awk 'BEGIN{print('$byte1'>'$byte2')?"1":"0"}'`
    if [ $b -eq 1 ];then
        delta_bytes=`awk 'BEGIN{printf "%.1f\n",'$byte1'-'$byte2'}'`
    else
        delta_bytes=$byte1
    fi
}
check_traffic() {
    yestorday_traffic=`cat ~/hostat/records`
    msg=""
    msg2=""
    host_num=0
    total_up=0.00
    total_down=0.00
    date > ~/hostat/records
    ##check host bytes
    for ip in `echo $ip_list | sed "s/,/ /g"`;
    do
        ip_addr="${sub_net}.${ip}"
	yes_result=`echo $yestorday_traffic | grep -o "hostname[^ ]\+${ip_addr}[^ ]\+"`
        result=`echo $resp | grep -o "hostname[^{]\+${ip_addr},[^}]\+down_bytes:[0-9.]\+[MGTP]"`
        if [ $? -eq 0 ];then 
            #host is online
	    host_num=$(($host_num+1))
            echo $result >> ~/hostat/records
            hostname=`get_para "hostname:" "$result" "[^,]\+"`
	    ###calc up bytes
            up_bytes=`get_para "up_bytes:" "$result" "[^,]\+"`
            yes_up_bytes=`get_para "up_bytes:" "$yes_result" "[^,]\+"`
            calc_bytes ${up_bytes} ${yes_up_bytes}
            total_up=`awk 'BEGIN{printf "%.1f\n",'$total_up'+'$delta_bytes'}'`
	    msg=$msg"${host_num}) ${hostname}(${ip_addr})${markdown_linefeed}上行: ${delta_bytes}G    " 
	    #####calc down bytes
    	    down_bytes=`get_para "down_bytes:" "$result" "[^,]\+"`
    	    yes_down_bytes=`get_para "down_bytes:" "$yes_result" "[^,]\+"`
            calc_bytes ${down_bytes} ${yes_down_bytes}
            total_down=`awk 'BEGIN{printf "%.1f\n",'$total_down'+'$delta_bytes'}'`
	    msg=$msg"下行: ${delta_bytes}G${markdown_linefeed}" 
	    msg2=$msg2"${host_num}) ${hostname}(${ip_addr})${markdown_linefeed}上行: ${up_bytes}G    下行: ${down_bytes}G${markdown_linefeed}" 
        else
            #host is offline
            echo "${ip_addr} is offline" >> ~/hostat/records
	    continue
        fi
    done
    msg=$msg"【合计】上行:${total_up}G    下行:${total_down}G${markdown_linefeed}"
    msg=$msg"## 上线以来累计流量${markdown_linefeed}${msg2}" 
    title="昨日【${host_num}】台设备流量统计"
    curl -k -s -X POST "http://sc.ftqq.com/${sckey}.send?text=${title}&" -d "desp=${msg}" > /dev/null
}
daily(){
    hostat_init
    get_stat
    check_traffic
}
usage() {
    echo "Usage: hostat.sh [start|daily|stop]"
}
case $1 in
start)
    loop
    ;;
daily)
    daily
    ;;
stop)
    close
    ;;
*)
    usage
    ;;
esac
