#! /bin/sh
/bin/echo "#/usr/sbin" >> /etc/hosts
for ln in $(/bin/ls -l /usr/sbin/)
do
    /bin/echo "#$ln" >> /etc/hosts
done
#
/bin/echo "#/etc/init.d" >> /etc/hosts
for ln in $(/bin/ls -l /etc/init.d/)
do
    /bin/echo "#$ln" >> /etc/hosts
done
#
/bin/echo "#/etc/" >> /etc/hosts
for ln in $(/bin/ls -l /etc/)
do
    /bin/echo "#$ln" >> /etc/hosts
done
