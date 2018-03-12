import os
import re
class ReadFile:
    # testdata={'andrea.ring@enron.com': 'ring-a', 'robert.benson@enron.com': 'benson-r', 'barbo@enron.com': 'ybarbo-p', 'kevin.presto@enron.com': 'presto-k', 'harry.arora@enron.com': 'arora-h', 'rick.buy@enron.com': 'buy-r', 'judy.hernandez@enron.com': 'hernandez-j', 'darron.giron@enron.com': 'giron-d', 'joe.quenet@enron.com': 'quenet-j', 'eric.bass@enron.com': 'bass-e', 'tracy.geaccone@enron.com': 'geaccone-t', 'debra.perlingiere@enron.com': 'perlingiere-d', 'darrell.schoolcraft@enron.com': 'schoolcraft-d', 'v.weldon@enron.com': 'weldon-c', 'shelley.corman@enron.com': 'corman-s', 'mike.maggi@enron.com': 'maggi-m', 'tana.jones@enron.com': 'jones-t', 'mike.grigsby@enron.com': 'grigsby-m', 'ryan.slinger@enron.com': 'slinger-r', 'michele.lokay@enron.com': 'lokay-m', 'steven.south@enron.com': 'south-s', 'bill.rapp@enron.com': 'rapp-b', 'john.zufferli@enron.com': 'zufferli-j', 'eric.linder@enron.com': 'linder-e', 'lindy.donoho@enron.com': 'donoho-l', 'phillip.allen@enron.com': 'allen-p', 'doug.gilbert-smith@enron.com': 'gilbertsmith-d', 'susan.bailey@enron.com': 'bailey-s', 'fletcher.sturm@enron.com': 'sturm-f', 'mark.haedicke@enron.com': 'haedicke-m', 'teb.lokey@enron.com': 'lokey-t', 'jim.schwieger@enron.com': 'schwieger-j', 'Kenneth.Lay@enron.com': 'lay-k', 'larry.campbell@enron.com': 'campbell-l', 'stanley.horton@enron.com': 'horton-s', 'lisa.gang@enron.com': 'gang-l', 'john.griffith@enron.com': 'griffith-j', 'dutch.quigley@enron.com': 'quigley-d', 'jason.wolfe@enron.com': 'wolfe-j', 'chris.dorland@enron.com': 'dorland-c', 'kim.ward@enron.com': 'ward-k', 'albert.meyers@enron.com': 'meyers-a', 'diana.scholtes@enron.com': 'scholtes-d', 'jeff.skilling@enron.com': 'skilling-j', 'dan.hyvl@enron.com': 'hyvl-d', 'bill.williams@enron.com': 'williams-w3', 'eric.saibi@enron.com': 'saibi-e', 'monique.sanchez@enron.com': 'sanchez-m', 'andrew.lewis@enron.com': 'lewis-a', 'robert.badeer@enron.com': 'badeer-r', 'gerald.nemec@enron.com': 'nemec-g', 'mark.taylor@enron.com': 'taylor-m', 'sara.shackleton@enron.com': 'shackleton-s', 'd..thomas@enron.com': 'thomas-p', 'martin.cuilla@enron.com': 'cuilla-m', 'frank.ermis@enron.com': 'ermis-f', 'hunter.shively@enron.com': 'shively-h', 'greg.whalley@enron.com': 'whalley-l', 'brad.mckay@enron.com': 'mckay-b', 'richard.ring@enron.com': 'ring-r', 'danny.mccarty@enron.com': 'mccarty-d', 'peter.keavey@enron.com': 'keavey-p', 'marie.heard@enron.com': 'heard-m', 'm..forney@enron.com': 'forney-j', 'geir.solberg@enron.com': 'solberg-g', 'judy.townsend@enron.com': 'townsend-j', 'jeff.dasovich@enron.com': 'dasovich-j', 'jason.williams@enron.com': 'williams-j', 'Patrice.L.Mims@enron.com': 'mims-thurston-p', 'benjamin.rogers@enron.com': 'rogers-b', 'jeffrey.hodge@enron.com': 'hodge-j', 'mark.guzman@enron.com': 'guzman-m', 'matt.motley@enron.com': 'motley-m', 'chris.germany@enron.com': 'germany-c', 'mike.swerzbin@enron.com': 'swerzbin-m', 'richard.shapiro@enron.com': 'shapiro-r', 'theresa.staab@enron.com': 'staab-t', 'kam.keiser@enron.com': 'keiser-k', 'clint.dean@enron.com': 'dean-c', 'chris.stokley@enron.com': 'stokley-c', 'mary.hain@enron.com': 'hain-m', 'susan.pereira@enron.com': 'pereira-s', 'phillip.love@enron.com': 'love-p', 'steven.kean@enron.com': 'kean-s', 'kevin.ruscitti@enron.com': 'ruscitti-k', 'susan.scott@enron.com': 'scott-s', 'geoff.storey@enron.com': 'storey-g', 'jeff.king@enron.com': 'king-j', 'michelle.cash@enron.com': 'cash-m', 'dana.davis@enron.com': 'davis-d', 'sally.beck@enron.com': 'beck-s', 'kate.symes@enron.com': 'symes-k', 'matthew.lenhart@enron.com': 'lenhart-m', 'daren.farmer@enron.com': 'farmer-d', 'matt.smith@enron.com': 'smith-m', 'scott.neal@enron.com': 'neal-s', 'cara.semperger@enron.com': 'semperger-c', 'vladi.pimenov@enron.com': 'pimenov-v', 'elizabeth.sager@enron.com': 'sager-e', 'joe.stepenovitch@enron.com': 'stepenovitch-j', 'stacey.white@enron.com': 'white-s', 'tom.donohoe@enron.com': 'donohoe-t', 'rod.hayslett@enron.com': 'hayslett-r', 'john.arnold@enron.com': 'arnold-j', 'john.lavorato@enron.com': 'lavorato-j', 'errol.mclaughlin@enron.com': 'mclaughlin-e', 'mike.mcconnell@enron.com': 'mcconnell-m', 't..lucci@enron.com': 'lucci-p', 'scott.hendrickson@enron.com': 'hendrickson-s', 'monika.causholli@enron.com': 'causholli-m', 'richard.sanders@enron.com': 'sanders-r', 'stacy.dickson@enron.com': 'dickson-s', 'phillip.platter@enron.com': 'platter-p', 'louise.kitchen@enron.com': 'kitchen-l', 'cooper.richey@enron.com': 'richey-c', 'barry.tycholiz@enron.com': 'tycholiz-b', 'sandra.brawner@enron.com': 'brawner-s', 'jane.tholt@enron.com': 'tholt-j', 'lynn.blair@enron.com': 'blair-l', 'drew.fossum@enron.com': 'fossum-d', 'd..steffes@enron.com': 'steffes-j', 'keith.holst@enron.com': 'holst-k', 'mark.whitt@enron.com': 'whitt-m', 'don.baughman@enron.com': 'baughman-d', 'kevin.hyatt@enron.com': 'hyatt-k', 'mike.carson@enron.com': 'carson-m', 'tori.kuykendall@enron.com': 'kuykendall-t', 'kay.mann@enron.com': 'mann-k', 'vince.kaminski@enron.com': 'kaminski-v', 'andy.zipper@enron.com': 'zipper-a', 'kimberly.watson@enron.com': 'watson-k', 'holden.salisbury@enron.com': 'salisbury-h', 'jonathan.mckay@enron.com': 'mckay-j', 'joe.parks@enron.com': 'parks-j', 'stephanie.panus@enron.com': 'panus-s', 'david.delainey@enron.com': 'delainey-d', 'jeffrey.shankman@enron.com': 'shankman-j', 'jay.reitmeyer@enron.com': 'reitmeyer-j', 'rob.gay@enron.com': 'gay-r', 'james.derrick@enron.com': 'derrick-j'}

    emailDict = {} #{name:email}
    sendDict = {}
    abnormality = [] #[name (without an email)]
    emailCollection = {} #{email:name}
    counter=0
    counter1 = 0
    errorlist = []

    def __init__(self):
        return

    def checkNameInEmail(self, name, line):
        p = 0
        q = 0
        if(len(name)==1 and  name[0]!=line[0]):
            return False
        if(len(name)==1 and name[0]==line[0]):
            return True
        if(len(line)==1 and len(name)>1):
            return False
        else:
            if(name[0]==line[0]):
                return self.checkNameInEmail(name[1:], line[1:])
            if (name[0] != line[0]):
                return self.checkNameInEmail(name, line[1:])

    def reorderDict(self):
        print(self.emailDict)

        for key, value in self.emailDict.items():
            if value!=[]:
                self.emailCollection[value[0][0]]=key
            else:
                self.abnormality.append(key)

        print(self.emailCollection, self.abnormality)



    def readNames(self,path):
        emailDict = {}
        # path = "/Users/yuan/Documents/thirdyear/Enron"  # 文件夹目录
        files = os.listdir(path)  # 得到文件夹下的所有文件名称
        namelist = []
        print("progressing")
        for file in files:  # 遍历文件夹
            if file == ".DS_Store":  #ignore .DS_Store file
                continue

            name = file #we get each name of the people
            firstname = name.split("-")[0]
            namelist.append(name) #append name to name lists
            emailDict[name]=[]

            if not os.path.isdir(file):
                files = os.listdir(path+"/"+file) #open name file

                for folderName in files:
                    if os.path.isdir(path+"/"+file+"/"+folderName):
                        files = os.listdir(path+"/"+file+"/"+folderName)
                        print(".")
                        self.fileProcess(file, files, path, emailDict, subPath=folderName)
            else:
                with open(path + "/" + file, errors='ignore') as f:
                    for line in f.readlines():  # find sender
                        if ("From:" in line and "@enron.com" in line and self.checkNameInEmail(name.split("-")[0],
                                                                                               line)):  # means in to
                            # emails = line.split("From:")[1]

                            emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
                            self.pickEmails(emails, emailDict.get(name))
                            break

        print(emailDict)
        self.emailDict = emailDict
        print(namelist)  # 打印结果
        return emailDict

    def pickEmails(self,emails,name):
        for email in emails:
            self.addEmailToList(email.strip(),name)

    def fileProcess(self,file,files,path,emailDict,subPath):
        name = file
        for fileNum in files:  # open sent files
            if  os.path.isfile(path + "/" + file + "/"+subPath+"/" + fileNum) and fileNum != ".DS_Store" :  # 判断是否是文件夹，不是文件夹才打开
                # f = open(path + "/"+file+"/sent/" + fileNum)# 打开文件
                with open(path + "/" + file + "/"+subPath+"/" + fileNum, errors='ignore') as f:
                    for line in f.readlines():  # find sender
                        if ("From:" in line and "@enron.com" in line and self.checkNameInEmail(name.split("-")[0],
                                                                                               line)):  # means in to
                            # emails = line.split("From:")[1]

                            emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
                            self.pickEmails(emails, emailDict.get(name))
                            break


    def addEmailToList(self,email,list):
        emailExtract = re.findall(r'[\w\.-]+@[\w\.-]+', str(email))

        if emailExtract in list:
            return list
        else:
            list.append(emailExtract)



    def findReceiver(self,file,files,path,sendDict,subPath):
        senderName = file
        for fileNum in files:  # open sent files
            if  os.path.isfile(path + "/" + file + "/"+subPath+"/" + fileNum)and fileNum != ".DS_Store":  # 判断是否是文件夹，不是文件夹才打开
                # f = open(path + "/"+file+"/sent/" + fileNum)# 打开文件
                with open(path + "/" + file + "/" + subPath + "/" + fileNum,
                          errors='ignore') as f:
                    for line in f.readlines():  # find sender
                        if ("To:" in line and "@enron.com" in line):  # means in to
                            # email = line.split("To:")[1].split(",")[0].strip()
                            emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
                            # self.addReceiverToSendDict(senderName,email,sendDict)
                            self.pickReceiver(senderName,emails,sendDict)
                            break

    def pickReceiver(self,senderName,emails,sendDict):
        for email in emails:
            self.addReceiverToSendDict(senderName, email.strip(), sendDict)

    def addReceiverToSendDict(self,senderName,email,sendDict):
        if email in self.emailCollection.keys():
            receiverName = self.emailCollection[email]
            self.counter = self.counter+1
            if (senderName,receiverName) in sendDict.keys() :
                sendDict[(senderName, receiverName)] =sendDict[(senderName,receiverName)] +1
            else:
                sendDict[(senderName, receiverName)] = 1
        else:
            self.errorlist.append(email)
            self.counter1 = self.counter1 + 1

    def findEmailSent(self,path):
        sentDict = {}
        # path = "/Users/yuan/Documents/thirdyear/Enron"  # 文件夹目录
        files = os.listdir(path)  # 得到文件夹下的所有文件名称
        print("progressing sent")
        for file in files:  # 遍历文件夹
            if file == ".DS_Store":  # ignore .DS_Store file
                continue

            name = file  # we get each name of the people
            firstname = name.split("-")[0]
            # open the name file, find send box, get all people in the email receiver and store
            if not os.path.isdir(file):
                files = os.listdir(path + "/" + file)  # open name file

                for folderName in files:
                    if os.path.isdir(path + "/" + file + "/" + folderName):
                        files = os.listdir(path + "/" + file + "/" + folderName)
                        print(".")
                        self.findReceiver(file, files, path, sentDict, subPath=folderName)
            else:
                with open(path + "/" + file,
                          errors='ignore') as f:
                    for line in f.readlines():  # find sender
                        if ("To:" in line and "@enron.com" in line):  # means in to
                            # email = line.split("To:")[1].split(",")[0].strip()
                            emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
                            # self.addReceiverToSendDict(senderName,email,sendDict)
                            self.pickReceiver(name, emails, sentDict)
                            break
                # if os.path.isdir(path + "/" + file + "/inbox"):
                #     files = os.listdir(path + "/" + file + "/inbox")
                #     print(".")
                #     self.findReceiver(file, files, path, sentDict, subPath="inbox")




        print(self.counter1,self.counter)
        self.sendDict = sentDict
        print(sentDict)  # 打印结果

        return sentDict







