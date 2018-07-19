#!/bin/bash

rsync -a -v --delete bouncer.deb marcus@$1:~
