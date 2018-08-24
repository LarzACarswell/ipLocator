#gets an IPv4 address and prints the contents of a JSON object from ip-api.com
#based off of similar command line tools
from urllib2 import urlopen
import socket,re,json,sys

def errorMessage(): #exit
    print "Incorrect arguments:\n\tusage: python ipLocator.py <IPv4 address or Domain Name> (Optional: <type [0|1]>)\n\t0: (default value) get information about an IP address.\n\t1: get IP address from domain name."
    sys.exit(0)
    
def supply(ipInput): #formats the URL with an IP
    return "http://ip-api.com/json/"+str(ipInput)

def getFirstSet(IP): #get the value of the first byte of the supplied IPv4 address
    first = re.findall("^\d{1,3}", RequestIP) #find first digit, returns a list of length 1
    try:
        setStr = "".join(first)
        return setStr
    except TypeError:
        print "-----------none-------------"
        sys.exit(0)
    
#argument checks
queryType=0
if len(sys.argv)>1: #check for first argument
    RequestIP = sys.argv[1]
    
    if len(sys.argv)>2: #check for second argument
        queryType=sys.argv[2]
        if len(queryType)==1: #make sure that the string is one character long
            try: #check for exceptions when constructing an int type
                if (int(queryType) not in [0,1]): #we only want this argument to be 1 or 0
                    errorMessage()  
                else:
                    queryType=int(queryType)
            except:
                errorMessage()
        else:
            errorMessage()
else: #else close
    errorMessage()

if getFirstSet(RequestIP) in ["192","10","172"]: #check for local IPs
    print "Local IP: "+RequestIP
else:
    if queryType==1:
        print socket.gethostbyname(RequestIP) #get IP from domain name
    else:
        url = supply(RequestIP) #IP information for a single element
        response = urlopen(url) #queries the website for IP information
        data = json.load(response) #returns a JSON object
        
        #now we print the data
        for types in data:
            outstr = str("%r"%types)+": "+str("%r"%data[types]) #outputs header: value, (example: Region: OH)
            print outstr.replace("u'","").replace("'","")
