import subprocess
from ConfigParser import SafeConfigParser
from StringIO import StringIO

def GetPorts(filename):
	f = file(filename);
	scp2 = SafeConfigParser()
	f.seek(0)
	scp2.readfp(f)
	sections = scp2.sections()
	ports={};
	for s in sections:
	    options = scp2.options(s)
	    try:
	    	PortNumber = scp2.get(s,"PortNumber");
	    	if(PortNumber):
	    		Connector =scp2.get(s,"Connector");
	    	ports[PortNumber]=Connector;
	    	pass
	    except Exception, e:
	    	print e
	    finally:
	   		pass
	return ports;
def GetAlivePort()：
	cmd = "netstat -anp tcp | find \"ESTABLISHED\""
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		cline = str(line).strip();
		print cline;
		items = cline.split();
		print items[2].split(":")[1]
ports = GetPorts("test.t2c");
	
