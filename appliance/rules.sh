#!/bin/bash

ufw --force reset
python3 /opt/bouncer/app/rules_scheduler.py /opt/bouncer/app/firewall.db
