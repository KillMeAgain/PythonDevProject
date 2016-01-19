# coding=utf-8
import urllib
import urllib2
import cookielib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

inst = "62006424"
user = "62000020000"
password = "8115608"
login_url = "http://10.2.69.164:7001/financial/worker.do?method=loginByGroup"
login_top = "http://10.2.69.164:7001/financial/forward.do?method=top_Forward"
login_left = "http://10.2.69.164:7001/financial/forward.do?method=left_Forward"
login_ss   = "http://10.2.69.164:7001/financial/forward.do?method=ss_Forward"
login_welcome = "http://10.2.69.164:7001/financial/forward.do?method=welcome"
query_url = "http://10.2.69.164:7001/financial/jbUserSingle.do?method=find_JbUserSingle"
query_page_url = "http://10.2.69.164:7001/financial/jbUserSingle.do?method=find_JbUserSinglePage"
query_card = "6217998200001637184"


#开始
cookie_jar = cookielib.CookieJar()
opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))

login_request = urllib2.Request(login_url)
login_request.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
login_request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
login_request.add_header('Accept-encoding','gzip, deflate')
login_request.add_header('Accept-language','zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4')
login_request.add_header('Cache-control','max-age=0')
login_request.add_header('Host','10.2.69.164:7001')
login_request.add_header('Origin','http://10.2.69.164:7001')
login_request.add_header('Referer','http://10.2.69.164:7001/financial/jbUserSingle.do?method=find_JbUserSinglePage')
login_request.add_header('Upgrade-Insecure-Requests','1')
login_request.add_data(urllib.urlencode({'groupId':inst,'username':user,'password':password,'image.x':34,'image.y':14}))
login_page = opener.open(login_request).read()
opener.open(login_top).read()
opener.open(login_left).read()
opener.open(login_ss).read()
opener.open(login_welcome).read()

find_page = urllib2.Request(query_page_url)
find_page.headers = login_request.headers
f = opener.open(find_page).read()
print find_page.get_method()
if re.search('session', f) == "None":
    print "Success"
else:
    print "Faild"

# query_request = urllib2.Request(query_url)
# query_request.add_header('User-agent', login_request.get_header('User-agent'))
# query_request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
# query_request.add_header('Accept-encoding','gzip, deflate')
# query_request.add_header('Accept-language','zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4')
# query_request.add_header('Cache-control','max-age=0')
# query_request.add_data('phone_No=&SHOWCOLS=true&account_No=6217998200001637184&SHOWCOLS=true&serviceType=&SHOWCOLS=true&txnSvrType=')
# query_page = opener.open(query_request)
# print query_page.read(2000000)