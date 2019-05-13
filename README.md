## NMFTA's Project Bouncer

![alt text](https://raw.githubusercontent.com/nmfta-repo/nmfta-bouncer/master/project-bouncer-small.png)


This is the README for the Bouncer Project.

This API has implemented features for IP and Geo Location based blocking.
It operates through the UFW firewall.
Changes made to the firewall's database are implimented every minute.

There is no admin or valid user account to start with. Add the --testing flag in the start.sh script to enable the registration page.

The ipv4geolist.csv was downloaded from http://lite.ip2location.com. The list is updated periodically so make sure to download the most recent version to keep the database upto date.

Terms of Use for ipv4geolist.csv can be viewed online at https://lite.ip2location.com/terms-of-use