#!/bin/sh

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
aniso8601==3.0.2
bcrypt==3.1.4
cffi==1.11.5
click==6.7
configparser==3.5.0
Flask==1.0.2
Flask-JWT-Extended==3.12.1
Flask-RESTful==0.3.6
Flask-SQLAlchemy==2.3.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
netaddr==0.7.19
pycparser==2.18
PyJWT==1.6.4
pytz==2018.5
six==1.11.0
SQLAlchemy==1.2.10
Werkzeug==0.14.1
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
