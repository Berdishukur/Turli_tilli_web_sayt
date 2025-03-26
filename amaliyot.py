
while True:
    xotira=30
    with open('my1.txt', 'a') as file:
        file.write("\n" + input("Ma'lumotlarni kiriting : "))
    with open('my1.txt', 'r') as file2:
        s1 = file2.read()
        uzunlik=len(s1)
        print(uzunlik)
    if uzunlik>xotira:
        print("sizda joy qolmadi ")
        break
