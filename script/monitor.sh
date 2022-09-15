#! /bin/sh
#for ip in $(cat ip_list | sed "/^#/d")
#vim-cmd vmsvc/getallvms
ip=192.168.10.10
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
    date >> /vmfs/volumes/625ee154-e817e0b2-65cf-00a0c9ee079d/scripts/monitor.log
    echo "IP:$ip is dead" >> /vmfs/volumes/625ee154-e817e0b2-65cf-00a0c9ee079d/scripts/monitor.log
    vim-cmd vmsvc/power.off 16 &> /dev/null
    sleep 10
    vim-cmd vmsvc/power.on 16 &> /dev/null
#else
    #echo "IP:$ip is alive"
fi
