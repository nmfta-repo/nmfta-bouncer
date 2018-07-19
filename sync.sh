#!/bin/bash

rsync -a -v --delete releases/bouncer.deb marcus@$1:~
