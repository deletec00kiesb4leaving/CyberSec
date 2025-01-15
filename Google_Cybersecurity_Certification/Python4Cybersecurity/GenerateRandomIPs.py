# This script is meant to generate random IP address
# I wrote it because I didn't want to used the IPs from the Lab

# Modules
import random
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description='A script that generates a number of randomized IP addresses.')
parser.add_argument('argument', type=int, help='Please provide the number of IP to be generated. **The value must be a number**')
parser.add_argument('filename', type=str, help='Please provide a name for the output file.')

# Parse the arguments
args = parser.parse_args()


# Variables
filename = args.filename
ip_addresses = []
ip_quantity = 0


# Functions
def generateNumber(first, last):
	number = random.randint(first, last)
	return number

def addToList(ip):
	ip_addresses.append(ip)

def generateAddress():
	# This var starts between 1 and 255 so the ip address doesn't start with a zero 0.XXX.XXX.XXX
	ip_address = str(generateNumber(1,255))

	for i in range(3):
		ip_address += '.' + str(generateNumber(0,255))
	
	return ip_address

def generateFile(filename, ip_list):
	content = ''
	for ip in ip_list:
		content += ip + ' '

	with open(filename, 'w') as file:
		file.write(content)


# Script
while ip_quantity < args.argument:
	addToList(generateAddress())
	ip_quantity += 1

generateFile(filename, ip_addresses)

print('Generated', args.argument, "IP address. Output: ./" + filename)
