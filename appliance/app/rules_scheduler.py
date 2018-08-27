"""Scheduler for platform"""

import sqlite3
import os, sys
if os.getuid() == 0:
    import ufw_interface as ufw
else:
    print("Must be run as root to interact with UFW")
    exit(-1)

def print_rules(conn):
    dump_whitelists(conn)
    print("")
    dump_blacklists(conn)

def do_rules(conn):
    cur = conn.execute("SELECT id, ipv4, remove FROM whitelist")
    print("Creating Whitelist Rules:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])
        ufw.run("allow from {}".format(row[1]))
        if row[2]:
            ufw.run("delete allow from {}".format(row[1]))

    cur = conn.execute("SELECT id, ipv4, remove FROM blacklist")
    print("Creating Blacklist Rules:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])
        ufw.run("deny from {}".format(row[1]))
        if row[2]:
            ufw.run("delete deny from {}".format(row[1]))

def dump_whitelists(conn):
    cur = conn.execute("SELECT id, ipv4 FROM whitelist")
    print("Dumping Whitelist Entries:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])

def dump_blacklists(conn):
    cur = conn.execute("SELECT id, ipv4 FROM blacklist")
    print("Dumping Blacklist Entries:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])

def main():
    #change location based on config
    #probably a good thing to put in the config file
    conn = sqlite3.connect(sys.argv[1])
    ufw.allow(8080)
    ufw.enable()
    do_rules(conn)

if __name__ == "__main__":
    main()
