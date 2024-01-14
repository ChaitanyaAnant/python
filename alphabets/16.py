with open("dictionary.txt","r")as f:
    data=f.read()
    listM=[]
    temp=data.split()
with open("count.txt","r")as f:
    for line in f:
        info1=line.rstrip().split(":")
        info1[1]=int(info1[1])
        
        print(info1)

def parse1(char1,qty1):
    listT=[]
    for word in temp:
        if word[0]==char1:
            if len(listT)<qty1:
                listT.append(word)
            else:
                break
    listM.append(listT)



   
    
    
