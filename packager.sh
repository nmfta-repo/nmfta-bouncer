#!/bin/sh

PY_DEPS="test"

echo "Removing Old Build Dir"
rm -rf bouncer/
rm releases/bouncer.deb

echo "Creating Relevant Directories"
mkdir -p bouncer/DEBIAN
mkdir -p bouncer/opt/bouncer
mkdir -p bouncer/opt/bouncer/app
mkdir -p bouncer/opt/bouncer/utils

cat > bouncer/DEBIAN/control << EOF
Package:bouncer
Version: 1.0
Maintainer: Drew Parker
Architecture: all
Depends: ufw
Depends-Build: python3-pip
Description: Project Bouncer Firewall Controller
EOF

cat > bouncer/opt/bouncer/pyreqs.txt << EOF
aniso8601==3.0.0
certifi==2018.4.16
chardet==3.0.4
click==6.7
Flask==1.0.2
Flask-JWT-Extended==3.10.0
Flask-RESTful==0.3.6
Flask-SQLAlchemy==2.3.2
idna==2.6
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
netaddr==0.7.19
passlib==1.7.1
PyJWT==1.6.4
python-iptables==0.13.0
pytz==2018.4
requests==2.18.4
six==1.11.0
SQLAlchemy==1.2.8
urllib3==1.22
Werkzeug==0.14.1
bcrypt==3.1.4
EOF

cat > bouncer/DEBIAN/postinst << EOF
cp /opt/bouncer/utils/bouncer-rest.service /etc/systemd/system/
cp /opt/bouncer/utils/bouncer-rules.service /etc/systemd/system/
cp /opt/bouncer/utils/bouncer-rules.timer /etc/systemd/system/
chmod +x /opt/bouncer/*.sh
systemctl enable bouncer-rest.service > /dev/null
systemctl enable bouncer-rules.timer > /dev/null
systemctl start bouncer-rest.service > /dev/null
systemctl start bouncer-rules.timer > /dev/null
echo "Installing python deps"
/usr/bin/pip3 install -r /opt/bouncer/pyreqs.txt > /dev/null
EOF

chmod +x bouncer/DEBIAN/postinst

echo "Copying files"
cp appliance/start.sh bouncer/opt/bouncer
cp appliance/rules.sh bouncer/opt/bouncer
cp appliance/app/* bouncer/opt/bouncer/app/
cp appliance/utils/* bouncer/opt/bouncer/utils/
cp appliance/default.conf bouncer/opt/bouncer

echo "Building"
dpkg-deb --build bouncer
mkdir -p releases
mv bouncer.deb releases/

echo "Done"
