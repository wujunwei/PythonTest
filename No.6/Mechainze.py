import mechanize


# test page
# def viewPage(url):
#     browser = mechanize.Browser()
#     page = browser.open(url)
#     source_code = page.read()
#     print(source_code)
# viewPage('http://www.syngress.con/')

# test proxy


def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)


ur = 'http://www.baidu.com/'
hideMeProxy = {'http': '216.155.139.115:3128'}
testProxy(ur, hideMeProxy)
