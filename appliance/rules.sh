#!/bin/bash

ufw --force reset
python3 /home/marcus/firewall/app/rules_scheduler.py
