import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('ubuntu', 'WUJUNWEI123')
        print('\n[*]' + str(hostname) + ' FTP Anonymous Login succeed')
        return True
    except Exception as e:
        print(e)
        return False

host = '115.159.222.116'
anonLogin(host)

