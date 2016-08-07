import nmap
#扫描端口是否开启


def nmapScan(tgtHost, tgtPort):
    try:
        nmScan = nmap.PortScanner()
        nmScan.scan(tgtHost, tgtPort)
        state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
        print(" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)
    except Exception as e:
        print(e)


def main():
    tgtHost = input("please input the host you want to scan: ")
    tgtPorts = []
    print("please input the ports you want to scan: (end with EOF !)")
    while True:
        temp = input()
        if temp == 'EOF':
            break
        tgtPorts.append(temp)
    if (tgtHost is None) | (tgtPorts[0] is None):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
