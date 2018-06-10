"""Scheduler for platform"""

import sqlite3
import os
if os.getuid() == 0:
    import iptc
else:
    print("Must be run as root to interact with iptables")
    exit(-1)

def print_rules(conn):
    dump_whitelists(conn)
    print("")
    dump_blacklists(conn)

def do_rules(conn):
    os.system("iptables --flush")
    cur = conn.execute("SELECT id, ipv4 FROM whitelist")
    print("Creating Whitelist Rules:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])
        rule = iptc.Rule()
        rule.protocol = "tcp"
        rule.src = row[1]
        match = iptc.Match(rule, "tcp")
        rule.add_match(match)
        rule.add_match(match)
        rule.target = iptc.Target(rule, "ACCEPT")
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        chain.insert_rule(rule)

    cur = conn.execute("SELECT id, ipv4 FROM blacklist")
    print("Creating Blacklist Rules:")
    for row in cur:
        print("id", row[0], "ipv4", row[1])
        rule = iptc.Rule()
        rule.protocol = "tcp"
        rule.src = row[1]
        match = iptc.Match(rule, "tcp")
        rule.add_match(match)
        rule.add_match(match)
        rule.target = iptc.Target(rule, "DROP")
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        chain.insert_rule(rule)

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
    conn = sqlite3.connect("src/firewall.db")
    do_rules(conn)
    #print_rules(conn)

if __name__ == "__main__":
    main()
