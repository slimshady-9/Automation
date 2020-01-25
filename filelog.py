import psutil;
import time;
import schedule;
import os;
import sys;

def hms():
	x=time.localtime();
	x=str(x.tm_hour)+str(x.tm_min)+str(x.tm_sec);
	return x;

def traverse(path):
	if not os.path.isabs(path):
		path=os.path.abspath(path);
	
	if not os.path.isdir("Automation"):
		os.mkdir("Automation");
	
	log=[];
	for F,SF,f in os.walk(path):
		for files in f:
			log.append(files);

	seperator="-"*45;

	try:

		logpath=os.path.join("Automation","log%s.txt"%hms());
	
		f=open(logpath,'w');
	
		f.write(seperator+"\n");
		f.write("Logs of files at "+str(time.ctime()));
		f.write(seperator+"\n");
	
		for x in log:
			f.write(x+"\n");

		f.close();

		print("File was created");

	except Exception:
		print("Failure in creation of File");


def main():
	
	schedule.every(1).seconds.do(traverse,path=sys.argv[1]);

	cnt=0;
	while 1:
		schedule.run_pending();
		cnt+=1;
		print(cnt);
		time.sleep(1);



if __name__ == '__main__':
	main()
