scan.py is a python module designed around the python-nmap library.
The purpose of this module is to easily scan a network, and
get an immediate report of all vulnerable services running
on a host, or hosts.

The module has three stages:
1. Discovery:
    Using python nmap to detect firewalls, discover hosts
    and store semi-stateful information about services
    running on a host or hosts.

2. CVE Query:
    This module will query an exploit database(tbd) and search
    for a vulnerability. If one is found, the source code is
    saved on the local machine in ./exploits/[port number]/[exploit]
    and a report is sent to the user.

    If the user specifies, this module will NOT create an outgoing
    connection to the exploit database, and will instead use exploits
    specified on the local machine. If none are found elsewhere,
    this module will search the local database for exploits
    matching the service in ./exploits/[port number]/

    If none are found, a warning will be issued to the user

3. Exploitation(Future):
    For now, the module will spawn a shell in the directory of the exploit
    and attempt to (compile and/or) launch the exploit

    In the future, I hope to convert a majority of the service exploits to
    python, to be able to be launched natively and immediately in a new
    python meterpreter-esque shell.