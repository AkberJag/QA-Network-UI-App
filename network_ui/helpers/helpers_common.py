import re


def validate_ip_address(ip_address):
    # validate the ip addess with re
    # https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(regex, ip_address):
        return True  # valid IP address
    return False
