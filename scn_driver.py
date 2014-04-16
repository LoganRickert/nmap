__author__ = 'eatsapizza'

class scanner:

    def __init__(self):
        self.ip = ""
        import nmap as nm
        self.nmapScannerObj = nm.PortScannerAsync()

    def getLoIP(self, device):

        if device == None:
            import netifaces
            device = netifaces.interfaces()[2]
        try:
            print("[*] obtaining network IP address on device: %s" % device)
            import netifaces
            ifaces = netifaces.ifaddresses(device)
            inet_iface = dict(ifaces).get(2)
            ipv4_addr = dict(inet_iface[0]).get('addr')
            print("[+] GOT: %s" % str(ipv4_addr))
            return ipv4_addr
        except Exception, ex:
            print "[--] CRITICAL ERROR: %s" % ex
            exit(0b100)



