print("-------Welcome to smart calculator---------")
print("-------My name is Jsrvis---------\n")
print("Before using scientific ooperations like = sin, cos, tan, etc..., write: help")
from math import *
while True:
    text = input("enter your queries...\n")

    lst1= ['add','ADD','addition','sum','plus','+']
    lst2= ['sub','subtraction','minus','-','less']
    lst3 = ['division','div','devide','/','dev']
    lst4 = ['mul','multiply','into','*','x']
    lst5 =['sin','sine','SIN']
    lst6 =['cos','COS']
    lst7 =['tan','TAN']
    lst8 =['log','LOG']
    lst9 = ['cot','kot','COT','KOT']
    lst10 =['sec','SEC']
    lst11 =['COSEC','cosec','cosine','COSINE']
    lst12 =['exit','EXIT','close','bye','by','goodbye','Goodbye']
    
#function will be called from here
    def check(self):
        x = self.split()
        y = len(x)
        if "help" in text:
            helpuser()
        if "name" in text:
            name()
        if "goodwork" in text:
            print("Thanku sir...")
        for i in range(y):
            for im in range(len(lst1)):
                if lst1[im] in x[i]:
                    ans=add(x,y)
                    print(ans)
                    break
                
            for im in range(len(lst2)):
                if lst2[im] in x[i]:
                    ans1 = SUB(x,y)
                    print(ans1)
                    break

            for im in range(len(lst3)):
                if lst3[im] in x[i]:
                    ans2 = dev(x,y)
                    print(ans2)
                    break

            for im in range(len(lst4)):
                if lst4[im] in x[i]:
                    ans3 = mul(x,y)
                    print(ans3)
                    break
                
            for im in range(len(lst5)):
                if lst5[im] == x[i]:
                    ans4 = sine(x,y)
                    print(ans4)
                    break

            for im in range(len(lst6)):
                if lst6[im] == x[i]:
                    ans5 = cose(x,y)
                    print(ans5)
                    break


            for im in range(len(lst7)):
                if lst7[im] == x[i]:
                    ans6 = tane(x,y)
                    print(ans6)
                    break

            for im in range(len(lst8)):
                if lst8[im] == x[i]:
                    ans7 = loge(x,y)
                    print(ans7)
                    break

            for im in range(len(lst9)):
                if lst9[im] == x[i]:
                    ans8 = cote(x,y)
                    print(ans8)
                    break

            for im in range(len(lst10)):
                if lst10[im] == x[i]:
                    ans9 = sece(x,y)
                    print(ans9)
                    break

            for im in range(len(lst11)):
                if lst11[im] == x[i]:
                    ans10 = cosece(x,y)
                    print(ans10)
                    break
            for im in range(len(lst12)):
                if lst12[im] in x[i]:               
                    print("I am glad that to work with you,Have a nice day sir... :)")
                    exit()
                
                 
#All the functions are defined here
    def cosece(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = (1/sin(con))
            except:
                pass

        return(t) 

    def sece(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = 1/cos(con)
            except:
                pass

        return(t) 
    

    def cote(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = cos(con)/sin(con)
            except:
                pass

        return(t)         
           
    def name():
        print("My name is Jarvis And i love maths...")

    def helpuser():
        print("\n> Hello sir, welcome to the world of calculations...")
        print("> I can do a lot of calculations for you, just give me problems to solve...")
        print("> List of problems i can solve...")
        print("1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n 5. sin ,cos ,tan ,tan ,cot ,sec ,cosec ,log ")
        print("\n> NOTE : don't use brackets while using sin ,cos ,tan ,cot ,sec ,cosec ,log... \ninstead of using (brackets), use spaces..\n")

    def loge(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = log(con)
            except:
                pass

        return(t)



    def tane(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = tan(con)
            except:
                pass

        return(t)


    def cose(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = cos(con)
            except:
                pass

        return(t)


    def sine(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = sin(con)
            except:
                pass

        return(t)
            
    

    def mul(self,temp):
        t = 1
        for j in range(temp):
            try:
                con = float(self[j])
                t = con * t
            except:
                pass

        return(t)
            


    def add(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = con + t
            except:
                pass

        return(t)
            

    def SUB(self,temp):
        t = 0
        for j in range(temp):
            try:
                con = float(self[j])
                t = con - t
            except:
                pass

        return(-t)

    def dev(self,temp):
        t = 1
        for j in range(temp):
            try:
                con = float(self[j])
                t = con / t
            except:
                pass

        return(t)
            


    check(text)
