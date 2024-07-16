#!/bin/sh

docker buildx build --platform linux/amd64 -t dannicool/docker-wechatbot-webhook:windows .