# file=open('my1.txt','r')
# s1=file.read()
# uzunlik=len(s1)
# file.close()
with open('my1.txt', 'a') as file:
    s1=file.read()
    print(s1)