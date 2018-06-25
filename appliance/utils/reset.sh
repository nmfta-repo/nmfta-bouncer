#!/bin/bash

rm -rf /home/marcus/.bouncer/
mkdir /home/marcus/.bouncer/
cp /home/marcus/firewall/default.conf /home/marcus/.bouncer/

chmod +x /home/marcus/firewall/start.sh
chmod +x /home/marcus/firewall/rules.sh
cp /home/marcus/firewall/utils/bouncer-* /etc/systemd/system/

systemctl enable bouncer-rest.service

systemctl start bouncer-rest.service
systemctl start bouncer-rules.timer
