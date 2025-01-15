# This is an a script made to automate file updates


# This function reads a file and returns it as a string
def read_file(filename):
	with open(filename, 'r') as file:
		content = file.read()
		return content

def update_file(filename, updated_list):
	ip_addresses = ''
	for each in updated_list:
		ip_addresses += each + ' '

	with open(filename, 'w') as file:
		file.write(ip_addresses)


# Variables
ip_list = read_file("allow_list.txt").split()
to_remove = read_file("remove_list.txt").split()


# Script
for ip in to_remove:
	if ip in ip_list:
		ip_list.remove(ip)

update_file("allow_list.txt", ip_list)
