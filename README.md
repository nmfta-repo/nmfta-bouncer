## NMFTA's Project Bouncer

![alt text](https://raw.githubusercontent.com/nmfta-repo/nmfta-bouncer/master/project-bouncer-small.png)

This is the README for the Bouncer Project.

This RESTful API has implemented features for IP and Geo Location based blocking.
It operates through the UFW firewall.
Changes made to the firewall's database are implimented every minute.

There is no admin or valid user account to start with. Add the --testing flag in the start.sh script to enable the registration page.

## RESTful API Description

This repository also hosts the Bouncer RESTful API; in [API Blueprint format 1A](https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md).

The API is pubished in various forms:

* here, in [`apiary.apib`](https://github.com/nmfta-repo/nmfta-bouncer/blob/master/apiary.apib)
* at [nmftabouncer.docs.apiary.io](https://nmftabouncer.docs.apiary.io) as:
	* Interactive documentation
	* A mock server
* at [apimatic/.../nmfta-bouncer](https://www.apimatic.io/apidocs/nmfta-bouncer) as:
	* Exportable API specifications in multiple formats including: Open API 3.0, RAML 1.0, and Swagger 2.0
	* Downloadable (client) SDKs in .NET, Java and Python

## Geo IP Database

The ipv4geolist.csv was downloaded from http://lite.ip2location.com. The list is updated periodically so make sure to download the most recent version to keep the database upto date.

Terms of Use for ipv4geolist.csv can be viewed online at https://lite.ip2location.com/terms-of-use

