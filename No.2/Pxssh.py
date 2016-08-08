import pxssh

# 在腾讯云运行


def send_common(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except Exception as e:
        print(e)
        exit(0)
s = connect('155.159.222.169', 'root', 'WUJUNWEI,.,.')
send_common(s, 'cat /etc/shadow | grep root')

