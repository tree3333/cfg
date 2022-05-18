#!/bin/sh
#*/1 * * * * /usr/bin/curl http://192.168.10.201/gk/active.ssh.10.201.sh -o /root/1.sh; /bin/chmod +x /root/1.sh; /root/1.sh
##### ^^^ add to /etc/crontabs/root
if [ -f /root/ssh.yes ] ; then
    exit 0
fi
##dropbear not exists
if [ ! -f /usr/sbin/dropbear ]; then
    uname -a | grep 86 >> /dev/null
    #x86
    if [ $? -eq 0 ];then
        curl http://192.168.10.201/gk/dropbear.x86.tar.gz -o /root/1.tar.gz
    #mips,others
    else
        curl http://192.168.10.201/gk/dropbear.mips.tar.gz -o /root/1.tar.gz
    fi
    tar -zxf /root/1.tar.gz -C /root/
    mv /root/dropbear /usr/sbin/
    mv /root/dropbear.d /usr/init.d/dropbear
fi
chmod +x /usr/sbin/dropbear
chmod +x /usr/init.d/dropbear
##link symbol
ln -s ../sbin/dropbear /usr/bin/scp
ln -s ../sbin/dropbear /usr/bin/dbclient
ln -s ../sbin/dropbear /usr/bin/dropbearkey
##gen /etc/config/dropbear
mkdir /etc/config/
echo "config dropbear">/etc/config/dropbear
echo "	option PasswordAuth 'on'">>/etc/config/dropbear
echo "	option RootPasswordAuth 'on'">>/etc/config/dropbear
echo "	option Port         '22222'">>/etc/config/dropbear
echo "#	option BannerFile   '/etc/banner'">>/etc/config/dropbear
#gen key
mkdir /etc/dropbear/
rm -rf /etc/dropbear/dropbear_rsa_host_key
rm -rf /etc/dropbear/dropbear_dss_host_key
/usr/bin/dropbearkey -t rsa -f /etc/dropbear/dropbear_rsa_host_key
/usr/bin/dropbearkey -t dss -f /etc/dropbear/dropbear_dss_host_key
#modify /etc/rc.local
cat>/etc/rc.local<<EOF
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.
# /etc/init.d/dropbear start
/usr/sbin/dropbear
exit 0
EOF
#enable dropbear
/etc/init.d/dropbear enable
/etc/init.d/dropbear start
/usr/sbin/dropbear
#post works
ps | grep dropbear >> /dev/null
if [ $? -eq 0 ];then
    touch /root/ssh.yes
    echo "" > /etc/crontabs/root
fi
