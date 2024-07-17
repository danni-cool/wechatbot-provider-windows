#!/bin/sh

docker build \
    --platform linux/amd64 \
    -t dannicool/wechatbot-provider-windows .

