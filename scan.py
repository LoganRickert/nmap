import subprocess

__author__ = 'eatsapizza'


def main():
    from optparse import OptionParser

    # Checks to make sure nmap is install on the machine. (Linux only)
    check_for_nmap()
    # Checks to make sure python-nmap is installed.
    check_for_python_nmap()
        
    print("[*] Loading optparse libs")

    help = """
        Welcome to Eatsa_pizza's scanning tool!
        Usage: ./scan.py [options] [host]
        NOTE! -l option requires avahi-daemon
    """
    cli_args = ""
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-l", "--local-net", dest="localnet",
                      action="store_true", default="False",
                      help="Use this option to scan the local network")

    parser.add_option("-i", "--interface", dest="iface", action="store", type="string",
                      help="Specify the interface to use i.e. wlan0, eth0...")

    #TODO: get port range
    parser.add_option("-p", "--port", dest="port_range", action="store", type="string",
                      help="Specify the port or port range to scan")

    #TODO: get IP range
    parser.add_option("-n", dest="ip_range", action="store", type="string",
                      help="IP range to scan. Valid formats are 1.1.1.1, 1.1.1.0-255, and 1.1.1.*")

    #TODO: add TCP port list
    parser.add_option("-t", "--tcp-ports-only", action="store_true",
                      dest="tcp_ports", help="Use this option to only scan top TCP ports")

    #Fragmentation
    parser.add_option("-f", "--firewall", dest="firewall", action="store_true",
                      default="true",
                      help="checks for possible existence of firewall")

    #adding argv and argc from  parser.parse_args()
    (options, args) = parser.parse_args()

    #if they want to scan the local net...
    if options.localnet:
        if options.iface is None:
            print("[*] Using default interface [\"wlan0\"], none specified")
        else:
            print("Attempting to use device [\"" + options.iface + "\"]...")
            cli_args += "--interface " + options.iface
        try:
            import scn_driver
        except ImportError, ie:
            print("[--] CRITICAL: import error, cannot locate scn_driver.py")
            exit(0b101)

        #initializing scanner object
        scn = scn_driver.scanner()
        
        #getting local network IP of the specified interface
        scn.getLoIP(options.iface)
        
        #Temporary conditional
        if options.port_range is None:
            beginningPort = 1
            endPort=444
        import infclass
        a = infclass.infocls(cli_args)

        scn.startScan(a)

def check_for_python_nmap():
    """ Checks to make sure nmap is installed on the machine. 
    If it is not, ask the user if they wish to install it and run the
    command 'sudo apt-get install python-nmap'.
    """
    try:
        import nmap
        print("[+] python-nmap is installed.")

    except ImportError, ex:
        print("[-] FATAL: Must have python-nmap installed\n"
              "for your best linux experience > sudo apt-get install python-nmap")

        ans = raw_input("Attempt to download python nmap? (Y/N): ")

        # If they answered yes, attempt to install nmap, else exit.
        if ans.upper() == "Y":
            install_python_nmap()
        elif ans.upper() == "YES":
            install_python_nmap()
        else:
            print("Quiting program...")
            exit(0)

def install_python_nmap():
    """ Attempt to install python nmap.
    """
    print("[*] Attempting to install python-nmap...")

    # Warning: Do not pass user input into this Popen with shell=True.
    process = subprocess.Popen("sudo apt-get install python-nmap", shell=True)
    print("[*] Installing...")
    process.wait()

    # If the subprocess had an error, tell the user and ask if they want to retry.
    if process.returncode != 0:
        print("[-] Operation was not successful!\n")

        ans = raw_input("Would you like to try again? (Y/N): ")

        if ans.upper() == "Y":
            install_python_nmap()
        elif ans.upper() == "YES":
            install_python_nmap()
        else:
            print("[-] Quiting program...")
            exit(0)

    print("[+] Successfully installed python-nmap.")

def check_for_nmap():
    """ Checks to see if nmap is installed. If it's not, ask if they would
    like to install it.
    """
    print("[*] Checking for nmap...")

    # Warning: Do not pass user input into this Popen with shell=True.
    process = subprocess.Popen("nmap -V > /dev/null", shell=True)
    process.wait()

    # If the subprocess had an error, tell the user and ask if they want to retry.
    if process.returncode == 127:
        print("[-] FATAL: Must have nmap installed\n"
              "for your best linux experience > sudo apt-get install nmap")

        ans = raw_input("Attempt to download nmap? (Y/N): ")

        if ans.upper() == "Y":
            install_nmap()
        elif ans.upper() == "YES":
            install_nmap()
        else:
            print("[-] Quiting program...")
            exit(0)
    elif process.returncode != 0:
        print("[-] Operation was not successful!\n")

        ans = raw_input("Would you like to try again? (Y/N): ")

        if ans.upper() == "Y":
            check_for_nmap()
        elif ans.upper() == "YES":
            check_for_nmap()
        else:
            print("[-] Quiting program...")
            exit(0)
    else:
        print("[+] nmap is installed.")

def install_nmap():
    """ Attempt to install nmap
    """
    print("[*] Attempting to install nmap...")

    # Warning: Do not pass user input into this Popen with shell=True.
    process = subprocess.Popen("sudo apt-get install nmap", shell=True)
    print("[*] Installing...")
    process.wait()

    # If the subprocess had an error, tell the user and ask if they want to retry.
    if process.returncode != 0:
        print("[-] Operation was not successful!\n")

        ans = raw_input("Would you like to try again? (Y/N): ")

        if ans.upper() == "Y":
            install_nmap()
        elif ans.upper() == "YES":
            install_nmap()
        else:
            print("[-] Quiting program...")
            exit(0)

    print("[+] Successfully installed python-nmap.")

if __name__ == "__main__":
    main()
