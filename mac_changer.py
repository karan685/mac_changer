#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    # interface = input("interface>")
    # new_mac = input("New MAC> ")

    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address for the system")

    # not going to use it because we are going to use it directly
    # interface = options.interface
    # new_mac = options.new_mac

    #not going to use because it is not be options, arguments are too available out these functions
    #(options, arguments) = parser.parse_args()

    (options, arguments) = parser.parse_args()

    if not options.interface:
        #code to handle error
        parser.error("[-] Please specify the interface to change its MAC address, use --help for more information")
    elif not options.new_mac:
        #code to handle error
        parser.error("[-] Please specify the new MAC address for the system, use --help for more information")

    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    # print("----------------------------------------------------------------")
    # #subprocess.call("ifconfig " + interface, shell=True)
    # result = subprocess.call(["ifconfig", interface])
    # mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    # print(mac_address_search_result.group(0))

def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = result.decode("utf-8")

    #print("-------------------------------------------------------------------------")
    # print(ifconfig_result)
    #mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Interface/Mac address")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC address: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")
