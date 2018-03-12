import pandas as pd
class Matrix:
    matrix = pd.DataFrame(index=[1], columns=['sender', 'senderEmail', 'receiver', 'receiverEmail', 'connection'],
                          data=[['','','','',0]])
    def printMatrix(self):
        print(self.matrix)

    def addEntry(self,sender,senderEmail,receiver,receiverEmail,connection):
        temp = pd.DataFrame([[sender,senderEmail,receiver,receiverEmail,connection]],columns=['sender', 'senderEmail', 'receiver', 'receiverEmail', 'connection'])
        self.matrix = self.matrix.append(temp,ignore_index=True)



r = Matrix()
r.addEntry("a","a","A","a",1)
print(r.printMatrix())