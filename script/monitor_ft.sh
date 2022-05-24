#! /bin/sh
sleep 1200
#for ip in $(cat ip_list | sed "/^#/d")
ip=192.168.10.9
while :
do
    ping -c 1 $ip &> /dev/null
    a=$?
    sleep 3
    ping -c 1 $ip &> /dev/null
    b=$?
    sleep 3
    ping -c 1 $ip &> /dev/null
    c=$?
    let d=$a+$b+$c
    if [ $d -gt 2 ]; then
        date >> /vmfs/volumes/625ee154-e817e0b2-65cf-00a0c9ee079d/scripts/ft.log
        echo "IP:$ip is dead" >> /vmfs/volumes/625ee154-e817e0b2-65cf-00a0c9ee079d/scripts/ft.log
        vim-cmd vmsvc/power.off 2 &> /dev/null
        sleep 10
        vim-cmd vmsvc/power.on 2 &> /dev/null
    #else
        #echo "IP:$ip is alive"
    fi
    sleep 300
done
