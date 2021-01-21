#!/usr/bin/env python

import subprocess

interface = input("Interface Name : ")
new_mac = input("Enter New Mac Adress : ")

print("--------------- Changing mac ----------------")
subprocess.call("ifconfig " + interface + " down" , shell=True)
subprocess.call("ifconfig " + interface + " hw ether " +  new_mac , shell=True)
subprocess.call("ifconfig " + interface + " up" , shell=True)

print("Mac adress of " + interface + " changed to " + new_mac )


#made by Arslan Manzoor