import json

class host():

    def __init__(self,hostip):
        self.hostip = hostip
        self.portlist = []

    def addport(self,port):
        self.portlist.append(port)

def printusedoc():
    print('''
    User Doc:
    load\tInputFilePath
    split\tInputFilePath\tOutputFilePath\tOutputFormat
    showall\t
    clear\t
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

def listallhost():

    global hostlist
    global hostdic

    for i in hostdic:
        print("----------------------------")
        print("[+]Host Ip: " + hostlist[int(hostdic[i][4:])].hostip)
        print("[+]Open Port:",end=" ")
        for k in hostlist[int(hostdic[i][4:])].portlist:
            print(k,end=" ")
        print()
        print("----------------------------")

if __name__ == '__main__':

    hostlist=[]
    hostdic = {}
    sum = 0

    while True:

        userinput = input("->")

        if userinput in ["help","h","?","HELP"]:

            printusedoc()

        elif userinput.split(" ")[0] in ["Load","load","LOAD"]:

            data = readjsonfile(userinput.split(" ")[1])
            jsondatatoclass(data)

        elif userinput in ["SHOWALL","showall","ShowAll","Showall","listall","LISTALL","LishAll","Listall"]:

            listallhost()

        elif userinput.split(" ")[0] in ["split","Split","SPLIT"]:

            hostlist=[]
            hostdic = {}
            sum = 0

            try:
                data = readjsonfile(userinput.split(" ")[1])
                jsondatatoclass(data)
                outputfile(userinput.split(" ")[2], userinput.split(" ")[3])
            except:
                printusedoc()

        elif userinput in ["clear","Clear","CLEAR"]:

            hostlist = []
            hostdic = {}
            sum = 0

