## Network Scanner

- Discover all devices on the Network.
- Displays their:
	- IP Address
	- MAC Address
	- Vendor's Name

#### API Used: 
[MAC Address Lookup](https://maclookup.app/)

#### Supports Platform:
Linux, Debain

### How to use:
- Convert the setup.sh into executable
	> **chmod 755 setup.sh**
- Run setup.sh
	> **./setup.sh**
- Run the Python Script with root privileges.
    > **sudo python3 network_scanner.py** 

#### Available Arguments:
- **-h or --help:** *Displays all the available options.*
- **-i or --interface**: *This option needs to be used as to define for which interface 
you want to scan the network.*
- **-r or --range:** *This option needs to be used as to define the network IP and 
the subnet mask. Example: 192.168.0.1/24 or 10.0.0.0/8 or 172.16.0.0/12*

- **Note:** You need to be connected to the network for scanning, as the program is based on ARP Request Protocol.

#### Color:
- **Green:** Successful.
- **Yellow:** In process.
- **System Color:** Result.
- **Red:** Unsuccessful or Errors. 

### Programming Language: Python 3.8

### Libraries Used:
- **subprocess:** The *subprocess* module allows you to spawn new processes, connect to their
input/output/error pipes, and obtain their return codes. Used to interact with command line
arguments.
- **argparse:** The *argparse* module makes it easy to write user-friendly command-line interfaces. The
program defines what arguments it requires, and argparse will figure out how to parse those out of
sys.argv.
- **re:** The *re (Regular Expression or regex)* module is used to search within a string using a sequence
of characters that define a search pattern. It is use to check the IP address enter by the user.
- **sys:** The *sys* module provides access to some variables used or maintained by the interpreter and
to functions that interact strongly with the interpreter.
- **scapy:** The *scapy* module enables the user to send, sniff and dissect and forge network packets.
This capability allows construction of tools that can probe, scan or attack networks.
- **requests:** The *requests* module takes all the work out of Python HTTP/1.1 — making your
integration with web services seamless. It is use to get the Vendor's Name using MAC address Lookup.
- **os:** The *os* module provides a portable way of using operating system dependent functionality.
- **time:** The *time* (Time access and conversions) module provides various time-related functions. It is used
to scan after every ceratin of time not continously.
- **termcolor:** The *termcolor* module is used for ANSII color formatting for
output in terminal.

#### Licensed: GNU General Public License, version 3

#### Developer Information:
- **Website:** [Hack Hunt](https://hack-hunt.blogspot.com/)
- **Contact:** hh.hackunt@gmail.com
- **Youtube:** [Hack Hunt](https://youtube.com/hackhunt) 
- **Instagram:** [hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
