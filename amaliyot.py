   # Filter
   # Reduce
   # Map
from functools import reduce
sonlar=[1,2,3,4,5,6,7,8,9]
result=reduce(lambda a,b:a if a>b else b,sonlar)
print((result))
# def even(n):
#     return (n>0)
# numbers1=[-1,3,12,-34,56]
# result=list(filter(even,numbers1))
# print(result)




# sonlar=[i for i in range(1,10) if i>5]
# print(sonlar)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango","olcha"]
# newList=[fruit.lower() for fruit in fruits if "a" in fruit[-1]]
# print(newList)
# for fruit in fruits:
#     if "a" in fruit:
#         newList.append(fruit)
# print(newList)
#