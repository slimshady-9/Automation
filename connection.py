import urllib.request
import urllib.error

#print(urllib.request.getproxies())

def ping():
	try:
		a=urllib.request.urlopen('https://github.com/slimshady-9',timeout=1);
		return True;
	except urllib.error.URLError:
		return False;

if(ping()):
	print("Internet connection established");
else:
	print("Error in connecting to server");
