import string,random
lchar="abcdefghijklmnopqrstuvwxyz"
uchar=lchar.upper()
spchar="#$%&*?@^"
#espchar="#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
num="1234567890"
#pas=raw_input("Enter anything: ")
#pas=list(pas)
#print(pas)
#paslen=len(pas)
password=[]
for i in range(0,10):
    char=i%5
    if(char==1):
        password.append(random.choice(lchar))
    elif(char==2):
        password.append(random.choice(uchar))
    elif(char==3):
        password.append(random.choice(spchar))
    elif(char==4):
        password.append(random.choice(num))
        
print("Password is " + ''.join(password))        
        
    
    

