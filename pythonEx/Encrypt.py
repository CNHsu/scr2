import random

class Encrypt:
    def __init__(self):
        self.code = [chr(i) for i in range(97,123)]       
        random.shuffle(self.code)
        self.alph = [chr(i) for i in range(97,123)]
        
    def __str__(self):
        return "code : " + "".join(self.code)
    
    def setCode(self,data):
        self.code = list(data)
        
    def getCode(self):
        return "".join(self.code)

    def toEncode(self,s):
        result = ""
        for i in s:
            if i in self.code:
                j = self.alph.index(i)
                result += self.code[j]
            else:
                result +=i            
        return "toEncode: "+result
    
    def toDecode(self,s):
        result = ""
        for i in s:
            if i in self.code:
                j = self.code.index(i)
                result += self.alph[j]
            else:
                result +=i
        return "toDecode: "+result[10:]
    
    
    
if __name__ == '__main__':
    s1= "The test of encrypt and decrypt"
    e= Encrypt()
 #   e.setCode()
    s2= e.toEncode(s1)
    s3= e.toDecode(s2)
    print(e)
    print("\n gestcode: ",e.getCode(),"\n",s1,"\n",s2,"\n",s3)

