#!/bin/sh
timestamp="$(date +'%b-%d-%y-%H:%M:%S')"
mkdir -p backup

sudo tar -czf ~/backup/backup_jenkins-${timestamp}.tar.gz ~/jenkins_home/