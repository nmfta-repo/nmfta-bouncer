#!/usr/bin/python

from tkinter import *
import requests
import sys

api_version = "v2"
host =  "http://localhost:8080" if len(sys.argv) < 2 else sys.argv[1]
access_token = ""

def login():
    global access_token
    username = "icon"#raw_input("Username: ")
    password = "test"#raw_input("Password: ")
    payload = (('username', username), ('password', password), ('grant_type', 'password'))
    data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
    if 'access_token' in data:
        access_token = data['access_token']
        print("good login")
    else:
        print("login failed:", data['message'])
        if "not exist" in data['message']:
            print("Autocreating new user [testing feature]")
            register()

def register():
    global access_token
    username = "icon"#raw_input("Username: ")
    password = "test"#raw_input("Password: ")
    payload = (('username', username), ('password', password))
    data = requests.post("{}/{}/register".format(host,api_version), data=payload).json()
    payload = (('username', username), ('password', password), ('grant_type', 'password'))
    data = requests.post("{}/{}/login".format(host,api_version), data=payload).json()
    if 'access_token' in data:
        access_token = data['access_token']
        print("good login")
    else:
        print("login failed:", data['message'])

window = Tk()
window.title("Bouncer Control")
try:
    login()
except:
    print("could not log in")
    sys.exit(-1)

lbl = Label(window, text="IP Addr", font=("Arial Bold", 14))
lbl.grid(column=0, row=0)

ip_box = Entry(window, width=20)
ip_box.grid(column=1, row=0)

def add_bl_entry():
    print("Adding blacklist entry {}".format(ip_box.get()))
    ip = ip_box.get()
    comments = "Generated using the GUI"
    payload = (('IPv4',ip),('Comments',comments))
    data = requests.post("{}/{}/blacklists/create".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print(data['Result']['Message'])

def add_wl_entry():
    print("Adding whitelist entry {}".format(ip_box.get()))
    ip = ip_box.get()
    comments = "Generated using the GUI"
    payload = (('IPv4',ip),('Comments',comments))
    data = requests.post("{}/{}/whitelists/create".format(host,api_version), data=payload, headers={"Authorization":"Bearer {}".format(access_token)}).json()
    print(data['Result']['Message'])

wl_btn = Button(window, text="Whitelist", command=add_wl_entry)
wl_btn.grid(column=0, row=2)

bl_btn = Button(window, text="Blacklist", command=add_bl_entry)
bl_btn.grid(column=1, row=2)

window.geometry("300x75")
window.mainloop()
