#!/bin/sh
#*/1 * * * * /usr/bin/curl http://gitee.com/tree333/cfg/raw/master/gk/active.ssh.sh -o /root/1.sh; /bin/chmod +x /root/1.sh; /root/1.sh
##### ^^^ add to /etc/crontabs/root
if [ -f /root/ssh.ok ] ; then
    exit 0
fi
##dropbear not exists
if [ ! -f /usr/sbin/dropbear ]; then
    uname -a | grep mips >> /dev/null
    #mips
    if [ $? -eq 0 ];then
        curl http://gitee.com/tree333/cfg/raw/master/gk/dropbear.mips.tar.gz -o /root/1.tar.gz
    #x86
    else
        curl http://gitee.com/tree333/cfg/raw/master/gk/dropbear.x86.tar.gz -o /root/1.tar.gz
    fi
    tar -zxf /root/1.tar.gz -C /root/
    chmod +x /root/*
    mv /root/dropbear /usr/sbin/
    mv /root/dropbear.d /usr/init.d/dropbear
fi
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
echo "" > /etc/crontabs/root
touch /root/ssh.ok
