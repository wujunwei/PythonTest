import ftplib

# 公司97服务器


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'sdfjafj@qq.com')
        print('\n[*]' + str(hostname) + ' FTP Anonymous Login succeed')
        return True
    except Exception as e:
        print(e)
        return False

host = '192.168.1.97'
anonLogin(host)

