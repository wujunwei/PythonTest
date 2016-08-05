import socket
#使用socket扫描端口，并获取占用，可能会被防火墙屏蔽


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n'.encode())
        results = connSkt.recv(100)
        print('[+]%d/tcp closed' % tgtPort)
        print('[+] '+str(results.decode()))
        connSkt.close()
    except Exception as e:
        print(e)
        return


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s' ; Unkonwn host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtHost)
        print('\n[+] Scan Results for :' + tgtName[0])
    except:
        print('\n[+] Scan Results for :' + tgtIp)
        socket.setdefaulttimeout(10)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    # parser = optparse.OptionParser("usage%prog " + "-H <target host> -p <target port>")
    # parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    # parser.add_option('-P', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    # (options, args) = parser.parse_args()
    # tgtHost = options.tgtHost
    # tgtPorts = str(options.tgtPort).split(', ')
    tgtHost = input("please input the host you want to scan: ")
    tgtPorts = []
    while True:
        temp = input("please input the ports you want to scan: (end with EOF !)")
        if temp == 'EOF':
            break
        tgtPorts.append(temp)
    if (tgtHost is None) | (tgtPorts[0] is None):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
    main()
