"""Scheduler for platform"""

import sqlite3

def dump_whitelists(conn):
    cur = conn.execute("SELECT id, ipv4 FROM whitelist")
    print "Dumping Whitelist Entries:"
    for row in cur:
        print "id", row[0]
        print "ipv4", row[1]

def dump_blacklists(conn):
    cur = conn.execute("SELECT id, ipv4 FROM blacklist")
    print "Dumping Blacklist Entries:"
    for row in cur:
        print "id", row[0]
        print "ipv4", row[1]

def main():
    conn = sqlite3.connect("src/firewall.db")
    dump_whitelists(conn)
    print ""
    dump_blacklists(conn)

if __name__ == "__main__":
    main()
