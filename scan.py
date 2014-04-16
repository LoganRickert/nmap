__author__ = 'eatsapizza'


def main():
    from optparse import OptionParser
    try:
        import nmap
        print("[+] Got python-nmap")

    except ImportError, ex:

        print("FATAL: Must have python-nmap installed\n"
              "aptitude> sudo apt-get install python-nmap")
        exit(0)
    print("[*] Loading optparse libs")

    help = """
        Welcome to Eatsa_pizza's scanning tool!
        Usage: ./scan.py [options] [host]
        NOTE! -l option requires avahi-daemon
    """

    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-l", "--local-net", dest="localnet",
                      action="store_true", default="False",
                      help="Use this option to scan the local network")

    #TODO: Look up interface specification
    parser.add_option("-i", "--interface", dest="iface", action="store", type="string",
                      help="Specify the interface to use i.e. wlan0, eth0...")

    #TODO: get port range
    parser.add_option("-p", "--port", dest="port_range", action="store", type="string",
                      help="Specify the port or port range to scan")

    #TODO: get IP range
    parser.add_option("-t", dest="ip_range", action="store", type="string",
                      help="IP range to scan. Valid formats are 1.1.1.1, 1.1.1.0-255, and 1.1.1.*")


    #Fragmentation
    parser.add_option("-f", "--firewall", dest="firewall", action="store_true",
                      default="true",
                      help="checks for possible existence of firewall")

    #adding argv and argc from  parser.parse_args()
    (options, args) = parser.parse_args()

    if options.localnet:
        if options.iface == None:
            print("[*] Using default interface, none specified")
        import scn_driver
        scn = scn_driver.scanner()




if __name__ == "__main__":
    main()

