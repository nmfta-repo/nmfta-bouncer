#!/bin/bash

rsync -a -v --delete appliance/ marcus@192.168.0.11:firewall
rsync -a -v --delete default.conf marcus@192.168.11:~/.bouncer/
