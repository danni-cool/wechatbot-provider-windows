#!/bin/sh

docker build \
    --platform linux/amd64 \
    --progress plain \
    -f docker/Dockerfile \
    -t dannicool/wechatbot-provider-windows:wc-3935 .
