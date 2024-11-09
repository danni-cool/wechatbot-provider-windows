#!/bin/sh

if [ -f /var/run/xrdp.pid ]; then
  rm /var/run/xrdp.pid
fi

/usr/sbin/xrdp

if [ -f /var/run/xrdp-sesman.pid ]; then
  rm /var/run/xrdp-sesman.pid
fi

/usr/sbin/xrdp-sesman

# Necesssary for docker
exec "$@"
