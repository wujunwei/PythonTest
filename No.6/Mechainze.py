import mechanize


# test page


# def viewPage(url):
#     browser = mechanize.Browser()
#     page = browser.open(url)
#     source_code = page.read()
#     print(source_code)
# viewPage('http://www.syngress.con/')

# test proxy


# def testProxy(url, proxy):
#     browser = mechanize.Browser()
#     browser.set_proxies(proxy)
#     page = browser.open(url)
#     source_code = page.read()
#     print(source_code)
#
#
# ur = 'http://www.baidu.com/'
# hideMeProxy = {'http': '216.155.139.115:80'}
# testProxy(ur, hideMeProxy)


# test userAgent


def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)
url = 'http://whatismyuseragent.dotdoh.com/'
userAgent = [('User-agent', 'Mozilla/5.0 (X11; U; ' + 'Linux 2.4.2-2 i586; en-us; m18) Gecko/20010131 Netscape6/6.01')]
testUserAgent(url, userAgent)
