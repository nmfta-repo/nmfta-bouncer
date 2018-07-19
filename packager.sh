#!/bin/sh

PY_DEPS="test"

echo "Removing Old Build Dir"
rm -rf bouncer/
rm bouncer.deb

echo "Creating Relevant Directories"
mkdir -p bouncer/DEBIAN

cat > bouncer/DEBIAN/control << EOF
Package:bouncer
Version: 0.1
Maintainer: Drew Parker
Architecture: all
Depends: ufw
Depends-Build: python3-pip
Description: Project Bouncer Firewall Controller
EOF

cat > bouncer/opt/bouncer/pyreqs.txt << EOF
appdirs==1.4.3
aurman==2.16.1
btrfsutil==1.0.0
CacheControl==0.12.5
chardet==3.0.4
colorama==0.3.9
distlib==0.2.7
distro==1.3.0
docopt==0.6.2
gufw==18.4.0
html5lib==1.0.1
idna==2.7
keyutils==0.5
lensfun==0.3.2
lockfile==0.12.2
msgpack==0.5.6
numpy==1.14.5
packaging==17.1
pexpect==4.6.0
Pillow==5.2.0
progress==1.4
psutil==5.4.6
ptyprocess==0.5.2
pyalpm==0.8
pycairo==1.17.0
pygobject==3.28.3
pyinotify==0.9.6
pyparsing==2.2.0
PyQt5-sip==4.19.12
pyserial==3.4
python-pam==1.8.4
python-xapp==1.2.0
pytoml==0.1.16
PyYAML==3.13
regex==2018.7.11
requests==2.19.1
retrying==1.3.3
scipy==1.1.0
setproctitle==1.1.10
sip==4.19.12
six==1.11.0
team==1.0
udiskie==1.7.5
ufw==0.35
urllib3==1.23
webencodings==0.5.1
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
pip install -r /opt/bouncer/pyreqs.txt
EOF

chmod +x bouncer/DEBIAN/postinst

mkdir -p bouncer/opt/bouncer
mkdir -p bouncer/opt/bouncer/app
mkdir -p bouncer/opt/bouncer/utils

echo "Copying files"
cp appliance/start.sh bouncer/opt/bouncer
cp appliance/rules.sh bouncer/opt/bouncer
cp appliance/app/* bouncer/opt/bouncer/app/
cp appliance/utils/* bouncer/opt/bouncer/utils/
cp appliance/default.conf bouncer/opt/bouncer

echo "Building"
dpkg-deb --build bouncer

echo "Done"
