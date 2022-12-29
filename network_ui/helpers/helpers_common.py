import re, ipaddress


def validate_ip_address(ip_address):
    # validate the ip addess with re
    # https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(regex, ip_address):
        return True  # valid IP address
    return False


def ip_mask_calculations(ip):
    net = ipaddress.IPv4Network(ip, False)

    if ip:
        try:
            if int(ip.rsplit("/")[1]) < 31:
                broadcast_addr = net.broadcast_address
                network_addr = net.network_address
                limit = f"{ net.network_address + 1} - {net.broadcast_address - 1}"
                return {
                    "broadcast_addr": broadcast_addr,
                    "network_addr": network_addr,
                    "limit": limit,
                }
        except:
            # yeah this is not the right way to handle errors
            pass
        return {"limit": ip}


def check_ip_belongs_subnet(ip, nw):
    if ip and nw:
        return ipaddress.ip_address(ip) in ipaddress.ip_network(nw, False)
