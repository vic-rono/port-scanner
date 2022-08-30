import nmap

sc = nmap.PortScanner()

print('My NMAP port scanner')

print('**********:-)****************')

ip_addy = input("Enter your IP address: ")

print("Yo Ip address is : ", ip_addy)

type(ip_addy)

res = input("""\n Enter the type of scan you want to execute
    a. SYN Scan
    b. UDP Scan
    c. Comprehensive Scan \n""")

print("You have selected: ", res)
#SYN(TCP) scanning
if res == 'a':
    print("nmap version: ", sc.nmap_version()) # to check the version of the nmap
    sc.scan(ip_addy, "1-1024", "-v -sS") # registered port range is between 1-1024 -v for verbosity -sS for sync scan
    print(sc.scaninfo()) 
    print("Your IP status: ", sc[ip_addy].state())
    print(sc[ip_addy].all_protocols())
    print("Open ports: ", sc[ip_addy]['tcp'].keys()) #for the number of ports opened.
#UDP scan
elif res == 'b':
    print("nmap version: ", sc.nmap_version())
    sc.scan(ip_addy, "1-1024", "-v -sU") #sU for UDP scans
    print(sc.scaninfo())
    print("Your IP status: ", sc[ip_addy].state())
    print(sc[ip_addy].all_protocols())
    print("Open ports: ", sc[ip_addy]['udp'].keys())
#Comprehensivescan

elif res == 'c':
    print("nmap version: ", sc.nmap_version())
    sc.scan(ip_addy, "1-1024", "-v -sU -sS -sV -sC -O -A")
    #-sS for tcp connecTIONS
    #-sV to  version info  of the machine
    #-A enables get the Os and version
    print(sc.scaninfo())
    print("Your IP status: ", sc[ip_addy].state()) #is up
    print(sc[ip_addy].all_protocols())
    print("Open ports: ", sc[ip_addy]['tcp'].keys())

elif res == 'd':
    print("INVALID!!!! Enter the valid options")


