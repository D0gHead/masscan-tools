import json
import sys

class host():

    def __init__(self,hostip):
        self.hostip = hostip
        self.portlist = []

    def addport(self,port):
        self.portlist.append(port)

def printusedoc():
    print('''
    User Doc:
    python masscan-tools.py InputFilePath OutputFilePath OutputFormat
    ''')

def readjsonfile(path):
    f = open(path,"r")
    data = f.read()
    f.close()
    jsondata = json.loads(data)
    return jsondata

def jsondatatoclass(data):
    global hostlist
    global hostdic
    global sum
    for i in data:
        if i['ip'] not in [x.hostip for x in hostlist]:
            exec("host%s = host(i['ip'])"%sum)
            exec("hostlist.append(host%s)"%sum)
            port = i['ports'][0]['port']
            exec("host%s.addport(str(%s))"%(sum,port))
            hostdic[i['ip']] = "host%s"%sum
            sum -= -1
        else:
            port = i['ports'][0]['port']
            exec("%s.addport(str(%s))" % (hostdic[i['ip']], port))

def outputfile(outfilepath,formatstr):
    f = open(outfilepath,"w")
    global hostlist
    global hostdic
    for i in hostlist:
        tmp = i.portlist
        for k in tmp:
            f.write(i.hostip + str(formatstr) + k + "\n")
    f.close()

hostlist=[]
hostdic = {}
sum = 0

if __name__ == '__main__':
    try:
        data = readjsonfile(sys.argv[1])
        jsondatatoclass(data)
        outputfile(sys.argv[2],sys.argv[3])
    except:
        printusedoc()
