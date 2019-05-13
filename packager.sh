#!/bin/sh

echo "Removing Old Build Dir"
rm -rf bouncer/

echo "Creating Relevant Directories"
mkdir -p bouncer/DEBIAN
mkdir -p bouncer/opt/bouncer
mkdir -p bouncer/opt/bouncer/src
mkdir -p bouncer/opt/bouncer/utils

cat > bouncer/DEBIAN/control << EOF
Package:bouncer
Version: 1.1
Maintainer: Drew Parker
Architecture: all
Depends: ufw, python3-pip
Depends-Build: python3-pip
Description: Project Bouncer Firewall Controller
EOF

cp appliance/src/requirements.txt bouncer/opt/bouncer/pyreqs.txt

cat > bouncer/DEBIAN/postinst << EOF
cp /opt/bouncer/utils/bouncer-rest.service /etc/systemd/system/
cp /opt/bouncer/utils/bouncer-rules.service /etc/systemd/system/
cp /opt/bouncer/utils/bouncer-rules.timer /etc/systemd/system/
chmod +x /opt/bouncer/*.sh
echo "Installing python deps"
/usr/bin/pip3 install -r /opt/bouncer/pyreqs.txt > /dev/null
openssl req -x509 -newkey rsa:4096 -nodes -out /opt/bouncer/dummy_cert.pem -keyout /opt/bouncer/dummy_key.pem -days 365 -subj="/C=US/ST=Denial/L=Default/O=Dis/CN=localhost"
systemctl enable bouncer-rest.service > /dev/null
systemctl enable bouncer-rules.timer > /dev/null
systemctl start bouncer-rest.service > /dev/null
systemctl start bouncer-rules.timer > /dev/null
EOF

chmod +x bouncer/DEBIAN/postinst

echo "Copying files"
cp appliance/start.sh bouncer/opt/bouncer
cp appliance/rules.sh bouncer/opt/bouncer
cp appliance/src/* bouncer/opt/bouncer/src/
cp appliance/utils/* bouncer/opt/bouncer/utils/
cp appliance/default.conf bouncer/opt/bouncer

echo "Building"
dpkg-deb --build bouncer
rm -rf bouncer/

echo "Done"
