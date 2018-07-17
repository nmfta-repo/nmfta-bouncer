#!/bin/bash

rsync -a -v --delete appliance/ marcus@$1:firewall
rsync -a -v --delete default.conf marcus@$1:~/.bouncer/
ssh marcus@$1 "chmod +x /home/marcus/firewall/utils/reset.sh"
