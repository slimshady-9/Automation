from sys import *
import webbrowser
import re
import urllib.request
import urllib.error

def ping():
	try:
		a=urllib.request.urlopen('https://github.com/slimshady-9',timeout=1);
		return True;
	except urllib.error.URLError:
		return False;

def Find(string):
	url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string);
	return url;

def WebLauncher(path):
	with open(path) as fp:
		for line in fp:
			print(line);
			url=Find(line);
			print(url);
			for str in url:
				webbrowser.open(str,new = 2)
def main():
	if(ping()):
		print("Internet connection established");
		WebLauncher(argv[1]);
	else:
		print("Error in connecting to server");

if __name__ == '__main__':
	main();
