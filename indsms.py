#!/usr/bin/python
import mechanize
import cookielib
import sys
br=mechanize.Browser()
cj=cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_robots(False)
br.addheaders=[('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US, rv:1.9.01) Gecko/2008071615 Fedora/16.0.1-1.fc9 Firefox/17=18.0.1')]

def gettxt():
    print "enter your message : "
    txt=""
    while True:
        line=raw_input()
        if "$" in line:
            break
        else:
            txt+=line+'\n'
    return txt

def loginsite():
    br.open('http://indyarocks.com/login')
    br.select_form(nr=0)
    br.form['LoginForm[username]']='manimarang'
    br.form['LoginForm[password]']='Shakira9'
    br.submit()
    if 'profile' in br.geturl():
        print 'login successfully'
    else:
        print 'failed to login'

def sendsms(mno,msg):
    print '>>> sending...'
    br.open('http://www.indyarocks.com/send-free-sms')
    print br.geturl()
    br.select_form(nr=1)
    br.form['FreeSms[mobile]']=mno
    br.form['FreeSms[post_message]']=msg
    br.submit()
    if 'login' in br.geturl():
        print 'failed'
    else:
        print '>>> sent'

def groupsms(book,txt):
    loginsite()
    f=open(book)
    for line in f.readlines():
        mno=line.split()[1]
        print 'sending to : '+line.split()[0]
        sendsms(mno,txt)
    print 'done'

def logoutsite():
    br.open('http://www.indyarocks.com/logout')
    print br.geturl()
    print 'logout successfully'
    sys.exit()


def main():
    if len(sys.argv[:])==2 and '.txt' in sys.argv[1]:
        msg=gettxt()
        groupsms(sys.argv[1],msg)
        logoutsite()
    if len(sys.argv[:])==2:
        msg=gettxt()
        loginsite()
        sendsms(sys.argv[1],msg)
        logoutsite()
    if '.txt' in sys.argv[1]:
        groupsms(sys.argv[1],sys.argv[2])
        logoutsite()
    if len(sys.argv[:])==3 and '.txt' in sys.argv[1]:
        groupsms(sys.argv[1],sys.argv[2])
        logoutsite()
    if len(sys.argv[:])==3:
        loginsite()
        sendsms(sys.argv[1],sys.argv[2])
        logoutsite()

if __name__=='__main__':
    main()

