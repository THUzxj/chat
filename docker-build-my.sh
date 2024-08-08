#!/bin/bash

VERSION=0.22.13

cp releases/${VERSION}/tinode-mysql.linux-amd64.tar.gz docker/tinode_my/

docker build --tag tinode/tinode-mysql:${VERSION} docker/tinode_my
