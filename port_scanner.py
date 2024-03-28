import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error: Invalid hostname"

    open_ports = []
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set timeout to 5 second
        result = s.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    if verbose:
        if ip_address != target:
            host_info = f"{target} ({ip_address})"
        else:
            host_info = ip_address

        result_str = f"Open ports for {host_info}\nPORT     SERVICE\n"
        for port in open_ports:
            service_name = common_ports.ports_and_services[port] if port in common_ports.ports_and_services else ""
            result_str += f"{str(port).ljust(9)}{service_name}\n"
        return result_str
    else:
        return open_ports