#! usr/bin/env python3

import sys
from termcolor import colored

try:
    import scapy.all as scapy
    import argparse
    import requests
    import os
    import time
    import subprocess
    import re
except KeyboardInterrupt:
    print(colored("\n[-] Exiting...\n", 'red'))
    sys.exit()


def scan_network(ip, interface):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_ips_data = scapy.srp(arp_request_broadcast, timeout=2, verbose=False, iface=interface)[0]

    targets = []

    for data in answered_ips_data:
        target_dict = {'ip': data[1].psrc, 'mac': data[1].hwsrc}
        targets.append(target_dict)

    return targets


def get_vendor(data):
    url = "https://api.maclookup.app/v2/macs/"

    for i in range(len(data)):
        request_url = url + data[i]['mac']
        get_data = requests.get(request_url)
        try:
            vendor = get_data.json()['company']
        except KeyError:
            vendor = "Unknown Vendor"
        data[i]['vendor'] = vendor

    return data


def print_data(data, count, ip, interface):
    print(colored("[+] Scanned IP Range: " + ip, 'yellow'))
    print(colored("[+] Scanned on Interface: " + interface, 'yellow'))
    print(colored("\n[+] Currently Scanning: Complete!", 'green'))
    print(colored("\n[+] Captured ARP Requests: {}".format(count), 'yellow'))
    print(colored("[+] Total number of hosts: {}".format(len(data)), 'yellow'))

    print("_" * 70)
    print(" {0:^12} \t {1:^17}    {2}".format("IP", "MAC Address", "MAC Vendor / Hostname"))
    print("-" * 70)

    for target in data:
        print(" {0:<12} \t {1:<17}   {2}".format(target['ip'], target['mac'], target['vendor']))


def call_function(ip, interface):
    scan_result = scan_network(ip, interface)
    scan_result = get_vendor(scan_result)
    return scan_result


def get_arguments():
    parser = argparse.ArgumentParser(prog="Network Scanner",
                                     usage="%(prog)s [options]\n\t[-r | --range] ip/mask\n\t[-i | --interface] "
                                           "interface_name",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Network Scanner v1.0 by Hack Hunt | <<<
    -------------------------------------""")

    parser._optionals.title = "Optional Argument"

    required_arguments = parser.add_argument_group("Required Arguments")
    required_arguments.add_argument('-r', '--range',
                                    dest='ip',
                                    metavar="",
                                    help="Specify network IP followed by range. Example: 192.168.0.1/24",
                                    required=True)

    required_arguments.add_argument('-i', '--interface',
                                    dest='interface',
                                    metavar='',
                                    help='Specify interface for scanning network.',
                                    required=True)

    args = parser.parse_args()
    check_input(args)
    return args


def check_input(args):
    try:
        subprocess.check_call(["sudo", "ifconfig", args.interface],
                              stdin=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL,
                              stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(colored("[-] Error! No interface (" + args.interface + ") found, use --help or -h for more info.", 'red'))
        sys.exit()

    if not re.match("\d+\.\d+\.\d+\.\d+/\d+", args.ip):
        print(colored("[-] Error! Invalid IP/Range, use --help or -h for more info.", 'red'))
        sys.exit()


def main():
    args = get_arguments()
    ip = args.ip
    interface = args.interface

    print(colored("[+] Initializing Network Scanner v1.0", 'green'))
    print(colored("[+/-] Loading...", 'yellow'))

    try:
        scan_results = call_function(ip, interface)
        count = len(scan_results)

        while True:
            os.system("clear")
            print_data(scan_results, count, ip, interface)
            time.sleep(8)

            scan = call_function(ip, interface)
            count += len(scan)

            for i in range(len(scan)):
                flag = True
                ip_check = scan[i]['ip']
                for j in range(len(scan_results)):
                    if ip_check == scan_results[j]['ip']:
                        flag = False

                if flag:
                    scan_results.append(scan[i])
    except KeyboardInterrupt:
        print(colored("\n[-] Exiting...\n", 'red'))
        sys.exit()



main()
