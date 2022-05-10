#!/bin/sh
#
mkdir /etc/config/
mkdir /etc/dropbear/
echo "config dropbear">/etc/config/dropbear
echo "	option PasswordAuth 'on'">>/etc/config/dropbear
echo "	option RootPasswordAuth 'on'">>/etc/config/dropbear
echo "	option Port         '22222'">>/etc/config/dropbear
echo "#	option BannerFile   '/etc/banner'">>/etc/config/dropbear
#
/bin/echo "127.0.0.1 localhost" > /etc/hosts
/bin/echo "192.168.10.30 gao.ke#lan" >> /etc/hosts
/bin/uname -a | while read x;
do
    /bin/echo "#$x" >> /etc/hosts
done
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

chmod +x /etc/init.d/dropbear
chmod +x /usr/sbin/dropbear
/etc/init.d/dropbear enable 
/etc/init.d/dropbear start
