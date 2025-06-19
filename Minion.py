def minion_game(string):
    S1=[]
    S2=[]
    S3=[]
    S4=[]
    str=string
    size=len(str)
    i=0
    while (i!=(size)):
        if str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i]=='U':
            S1.append(str[i])
            S3.append(string.index(str[i]))
            str=str.replace(str[i],'')
        else :
            S2.append(str[i])
            S4.append(string.index(str[i]))
            str=str.replace(str[i],'')

        size=len(str)

    N1=0
    for i in range(len(S3)):
        N1+=string.count(S1[i])
        substr1=S1[i]
        j=S3[i]+1
        while (j!=(len(string))):
            substr1+=string[j]
            N1+=string.count(substr1)
            j+=1    

    N2=0
    for i in range(len(S4)):
        N2+=string.count(S2[i])
        substr1=S2[i]
        j=S4[i]+1
        while (j!=(len(string))):
            substr1+=string[j]
            N2+=string.count(substr1)
            j+=1    


    if (N1<N2):
        print (f"Stuart {N2}")
    elif (N1>N2):
        print (f"Kevin {N1}")
    else:
        print ("Draw")

def find_substr(string,substr):  
    pass


if __name__ == '__main__':
    s = input()
    minion_game(s)