
import random
son=random.randint(1,100)
qadam=0
while True:
    qadam+=1
    tanlov=int(input("Tanlov uchun son kiriting : "))
    if tanlov==son:
        print("O'ylangan sonni" ,qadam," ta urunishda  topdingiz!!!")
        break
    elif tanlov<(son/2):
        print("Juda past.")
    elif tanlov>(2*son):
        print("Juda baland.")
    elif tanlov>son:
        print("Ozgina baland.")
    elif tanlov<son:
        print("Ozgina past.")