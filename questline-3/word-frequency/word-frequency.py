def display():
    f=open("words.txt","r")
    s=f.read()
    f.close()
    L=s.split()
    freq={}
    for i in L:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for j in sorted(freq):
      print(j,"→",freq[j])
display()
