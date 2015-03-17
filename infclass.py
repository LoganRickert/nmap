class infocls:
  _HASHLIB_MD5
  try:
    import hashlib
    _HASHLIB_MD5 = hashlib.md5()
  except ImportError, ie:
    print "[-] CRITICAL: missing python hashlib... exiting..."
    exit(-1337) #lol

  #key is perhaps md5 of str(host_addr) ?
  #maybe there's a better way or a case that this would not be preferable

  #List of pairs in the format { host_addr : key }
  devAddrPair = []
  #arguments to pass to the nmap command line
  args = []

  #store JSON objects representing a host
  #The host should be in the format { host_addr : key }
  #The scan will then be { JSON : key }
  #Where key is a unique ID correlating host to JSON for use later
  scans = []
  
  def __init__(self, args):
    pass

  def genKey(self, _input):
    try:
      _HASHLIB_MD5.update(_input)
      return _HASHLIB_MD5.update()
    except Exception as detail:
      print "[-] DANGER WILL ROBINSON: something went gravely wrong\n" + detail

  def addPair(self, pair):
    if not pair:
      return
    else:
      self.devAddrPair.insert(pair)
      #this mayhaps wont work... probably not...
    
