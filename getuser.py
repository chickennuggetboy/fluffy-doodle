#!/usr/bin/env python

#get the username from a prompt
username = raw_input("Login: >> ")

#list of allowed users
user1 = "admin@wellmanage.com"
user2 = "guest@wellmanage.com"

#control that the user belongs to the list of allowed users
if username == user1:
    print "Access granted boss"
elif username == user2:
    print "Welcome to the Wellmanage.com ERP system"
else:
    print "Access denied"
