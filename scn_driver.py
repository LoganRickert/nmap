__author__ = 'eatsapizza'

class scanner:

    def __init__(self):

        import nmap as nm
        self.nmapScannerObj = nm.PortScannerAsync()

    def getLoIP(self, device):

        try:
            print("[*] obtaining network IP address on device: %s" % device)
            import netifaces

            if(device is None):
                device = netifaces.interfaces()[2]
            #getting interface list
            ifaces = netifaces.ifaddresses(device)

            #using unix AF_INET constant (2) and obtaining dict of IP info from
            #specified interface(iface)
            inet_iface = dict(ifaces).get(2)

            #getting actual network address
            ipv4_addr = dict(inet_iface[0]).get('addr')
            print("[+] Local IP is: %s" % str(ipv4_addr))
            return ipv4_addr
        except Exception, ex:
            print "[-] CRITICAL ERROR: %s" % ex
            print("\tAre you using the right interface?")
            exit(0b101)

    def get_ports(self, ports):
        ports = str(ports)
        if ports.__contains__("-"):

            #split the string with a dash as a delimiter
            ports = ports.replace("-", " ")
            portList = ports.split()

            #testing to see
            if len(portList) < 2:
                print("[-] CRITICAL: invalid port argument length.")
            if portList[0] or portList[1] is not int:
                print("[-] CRITICAL: Ports specified must be integers.")
                exit(0b111)


