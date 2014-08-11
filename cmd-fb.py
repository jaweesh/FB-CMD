'''
Name : Facebook From  Command line
Author : Khaled Farah
Version : 0.0.1

Date: 3/18/2014
'''
import mechanize , cookielib , sys 
from bs4 import BeautifulSoup 
br = mechanize.Browser()
def login(br) : 
	br.select_form(nr=0)
	email = raw_input("[*] Please Enter your email :")
	password = raw_input("[*] Please Enter your password :") 
	br.form["email"]=email 
	br.form["pass"] = password
	br.submit()

print '''\n 
   mmm  m    m mmmm          mmmmmm mmmmm 
 m"   " ##  ## #   "m        #      #    #
 #      # ## # #    #        #mmmmm #mmmm"
 #      # "" # #    #  """   #      #    #
  "mmm" #    # #mmm"         #      #mmmm"
                '''
                                                                     
          
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.addheaders = [('User-agent',' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'),
                 ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                 ('Accept-Encoding', 'gzip,deflate,sdch'),                  
                 ('Accept-Language', 'en-US,en;q=0.8'),                     
                 ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')]
try : 
	br.open("https://m.facebook.com")
	login(br)
	res = br.response().read()
	while "Create Account" in res   : 
		print "[-] Error loggin , please re-enter ur email & password"
		login(br)
		res = br.response().read()
except : 
	print "[-] error connecting to Facebook , try again later " 
	exit()
	

print "[+] you are in "
while 1 : 
 	
	a = raw_input("[*] f to fill forms , l for click links ,t to display text ,  b to go back , r to reload and e to exit : ")
	if a=="f" : 
		try : 
			for form in br.forms() : 
				print form 
			f =  raw_input("enter the number of form :") 
			br.select_form(nr=int(f))
			b ="select" 
			while b != "" : 
				b = raw_input(" ur data seprated by a : ")
				statment =b.split(":")
				if b != "" : 
					br.form[str(statment[0])] = str(statment[1])
			br.submit()
		except : 
			pass
	elif a=="l" : 
		try :
			for link in br.links() : 
				print link.text+" " ,
			print 
			link2 = raw_input("enter link to click ")
			link = br.click_link(text=link2)
			br.open(link)
		except : 
			pass
	elif a=="t" : 

		bs = BeautifulSoup(br.response().read() , "lxml") 
		for i in bs.find_all("span") :
			if i == " "  : 
				pass  
			else : 
				print i.text 
	elif a=="r" : 
			br.reload() 
	elif a=='b' : 
		br.back() 
	elif a=='e' : 
		br.close()
		exit()

		
	
br.close()
               

       
        
