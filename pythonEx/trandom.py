import Encrypt
from datetime import date
from math import log
import re


print(date.today())
print(log(1024,2))
print (re.search("o","dog"))
      
e = Encrypt.Encrypt()
s1= "The big big bad man"
 #   e.setCode()
s2= e.toEncode(s1)
s3= e.toDecode(s2)
print(e)
print("\n gestcode: ",e.getCode(),"\n",s1,"\n",s2,"\n",s3)
