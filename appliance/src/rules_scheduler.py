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
    cur = conn.execute("SELECT id, ipv4, remove FROM iptable WHERE lt=\"wl\"")
    print("Creating Whitelist Rules:")
    for row in cur:
        ufw.run("allow from {}".format(row[1]))
        if row[2]:
            conn.execute("DELETE FROM iptable WHERE id={}".format(row[0]))
            conn.commit()
            ufw.run("delete allow from {}".format(row[1]))

    cur = conn.execute("SELECT id, ipv4, remove FROM iptable WHERE lt='bl'")
    print("Creating Blacklist Rules:")
    for row in cur:
        ufw.run("deny from {}".format(row[1]))
        if row[2]:
            conn.execute("DELETE FROM iptable WHERE id={}".format(row[0]))
            conn.commit()
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
<<<<<<< HEAD
    ufw.allow(22)
=======
>>>>>>> d3ce74130c10ccc1af941f0eed3ef471b51b91b0
    ufw.enable()
    do_rules(conn)

if __name__ == "__main__":
    main()
