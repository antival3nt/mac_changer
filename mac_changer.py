#!/usr/bin/env python3

# Imports
import subprocess
import sys
import os
import random

print("=" * 60)
print("This program is written by: Pl4gueDoct0r")
print("Used for: Changing your MAC address")
print("Your not allowed to share this program!")
print("=" * 60)
    
ans = True
while ans:
    print("""
    1. Change to random MAC
    2. Set MAC address to original MAC
    3. Enter specific MAC
    q. Quit
    """)
    ans = input("Please Select: ")
    
    if ans=="1":
        print("Change to random MAC.")
        interface = input("Which interface are you using? (wlan0, eth0 etc.): ")

        # Functions
        def rand_mac():
            return "%02x:%02x:%02x:%02x:%02x:%02x" % (
                random.randint(0, 127) * 2,
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
                )

        def changeMAC():
            new_mac = rand_mac()

            # Magic happens
            print("[+] Changing MAC address for:", interface)
            print("[+] New MAC address:", new_mac)

            # Change MAC address
            subprocess.call("ifconfig " + interface + " down", shell=True)
            subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
            subprocess.call("ifconfig " + interface + " up", shell=True)

        # If orig_MAC file exists
        if os.path.isfile('./orig_MAC'):
            changeMAC()
        else:
            print("Fetching original MAC address")
            orig_mac = subprocess.getoutput("LANG=C ifconfig " + interface + " | grep -o 'ether [[:xdigit:]:]*'")
            orig_mac = orig_mac.split(" ")
            original_stdout = sys.stdout # Save a reference to the original standard output
            with open('orig_MAC', 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print(orig_mac[1])
                sys.stdout = original_stdout # Reset the standard output to its original value
            print("Original MAC address saved to file: orig_MAC")
            changeMAC()
            ans = None
            
    elif ans=="2":
        print("Set MAC address to original MAC.")
        interface = input("Which interface are you using? (wlan0, eth0 etc.): ")
        print("Fetching original MAC address")
        with open('orig_MAC', 'r') as file:
            orig_mac = file.read()
            
        def changeOrigMAC():
            
            # Magic happens
            print("[+] Changing MAC address for:", interface)
            print("[+] Original MAC:", orig_mac)

            # Change MAC address
            subprocess.call("ifconfig " + interface + " down", shell=True)
            subprocess.call("ifconfig " + interface + " hw ether " + orig_mac, shell=True)
            subprocess.call("ifconfig " + interface + " up", shell=True)
        changeOrigMAC()
        print("[-] orig_MAC file deleted")
        os.remove("orig_MAC")
        ans = None
        
    elif ans=="3":
        interface = input("Which interface are you using? (wlan0, eth0 etc.): ")
        spec_mac = input("Enter specific MAC 'xx:xx:xx:xx:xx:xx': ")

        # Function for specific MAC
        def changeSpecMAC():

            # Magic happens
            print("[+] Changing MAC address for:", interface)
            print("[+] New MAC address:", spec_mac)

            # Change MAC address
            subprocess.call("ifconfig " + interface + " down", shell=True)
            subprocess.call("ifconfig " + interface + " hw ether " + spec_mac, shell=True)
            subprocess.call("ifconfig " + interface + " up", shell=True)

        # If orig_MAC file exists
        if os.path.isfile('./orig_MAC'):
            changeSpecMAC()
        else:
            print("Fetching original MAC address")
            orig_mac = subprocess.getoutput("LANG=C ifconfig " + interface + " | grep -o 'ether [[:xdigit:]:]*'")
            orig_mac = orig_mac.split(" ")
            original_stdout = sys.stdout # Save a reference to the original standard output
            with open('orig_MAC', 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print(orig_mac[1])
                sys.stdout = original_stdout # Reset the standard output to its original value
            print("Original MAC address saved to file: orig_MAC")
            changeSpecMAC()
            ans = None
            
    elif ans=="q":
        print("\n Goodbye") 
        ans = None
        
    else:
        print("\n Not Valid Choice Try again")