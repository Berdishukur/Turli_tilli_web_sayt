import copy
sonlar=[[2,3,4,5,6],[-3,-5,-7,-9]]
sonlar2=copy.deepcopy(sonlar)
sonlar2[0][0]=90
print(sonlar2)
print(sonlar)