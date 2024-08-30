#!/bin/bash

VERSION=0.22.13-2-gbe0da60a

./build-my.sh

cp releases/${VERSION}/tinode-mysql.linux-amd64.tar.gz chat_experiment/tinode_my/

docker build --tag tinode/tinode-mysql:${VERSION} chat_experiment/tinode_my --no-cache

docker build --tag tinode/tinode-chatbot:${VERSION} chat_experiment/chatbot
