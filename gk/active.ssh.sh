#!/bin/sh
#0 22 * * * /usr/bin/nc 192.168.10.6 4444 >/root/1.tar.gz
#1 22 * * * /bin/tar -zxf /root/1.tar.gz -C /root/
#2 22 * * * /root/1.sh
##### ^^^ add to /etc/crontabs/root
#dropbear exists
if [ -f /usr/sbin/dropbear ]; then
    echo "1.sh exists"
fi
if [ ! -f /root/1.sh ]; then
    echo "1.sh not exists"
fi
mkdir /etc/config/
mkdir /etc/dropbear/
echo "config dropbear">/etc/config/dropbear
echo "	option PasswordAuth 'on'">>/etc/config/dropbear
echo "	option RootPasswordAuth 'on'">>/etc/config/dropbear
echo "	option Port         '22222'">>/etc/config/dropbear
echo "#	option BannerFile   '/etc/banner'">>/etc/config/dropbear
#
chmod +x /root/*
cp /root/dropbear /usr/sbin/
cp /root/dropbear.d /etc/init.d/dropbear
ln -s ../sbin/dropbear /usr/bin/scp
ln -s ../sbin/dropbear /usr/bin/dbclient
ln -s ../sbin/dropbear /usr/bin/dropbearkey
#
rm -rf /etc/dropbear/dropbear_rsa_host_key
rm -rf /etc/dropbear/dropbear_dss_host_key
/usr/bin/dropbearkey -t rsa -f /etc/dropbear/dropbear_rsa_host_key
/usr/bin/dropbearkey -t dss -f /etc/dropbear/dropbear_dss_host_key
#
cat>/etc/rc.local<<EOF
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.
# /etc/init.d/dropbear start
/usr/sbin/dropbear
exit 0
EOF
#
chmod +x /etc/init.d/dropbear
/etc/init.d/dropbear enable
/etc/init.d/dropbear start
/usr/sbin/dropbear
###ls -l to /etc/hosts
#
/bin/echo "127.0.0.1 localhost" > /etc/hosts
/bin/echo "192.168.10.30 gao.ke#lan" >> /etc/hosts
/bin/echo "#/usr/sbin" >> /etc/hosts
/bin/ls -l /usr/sbin/ | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
/bin/echo "#/usr/bin" >> /etc/hosts
/bin/ls -l /usr/bin/ | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
#
/bin/echo "#/etc/init.d" >> /etc/hosts
/bin/ls -l /etc/init.d/ | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
#
/bin/echo "#/etc/" >> /etc/hosts
/bin/ls -l /etc/ | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
#
/bin/echo "#/etc/dropbear" >> /etc/hosts
/bin/ls -l /etc/dropbear | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
#
echo "#find /etc" >> /etc/hosts
find /etc | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
#
echo "#/root/" >> /etc/hosts
/bin/ls -l /root/ | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done

