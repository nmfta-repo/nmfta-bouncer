#!/bin/bash

rsync -a -v --delete appliance/ marcus@centurion:firewall
