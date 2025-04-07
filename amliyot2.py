g=['🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎','🍎']
def jadval():
    print(f"""
    | {g[0]} | {g[1]} | {g[2]} |  {g[3]} |
    | {g[4]} | {g[5]} | {g[6]} |  {g[7]} |
    | {g[8]} | {g[9]} | {g[10]} |  {g[11]} |
    | {g[12]} | {g[13]} | {g[14]} |  {g[15]} |


    """)
def shart(s):
    return (g[0] == g[1] == g[2] == s or g[3] == g[4] == g[5] == s or g[6] == g[7] == g[8] == '🐢' or \
    g[0] == g[3] == g[6] == '🐢' or g[1] == g[4] == g[7] == '🐢' or g[2] == g[5] == g[8] == '🐢' or \
    g[0] == g[4] == g[8] == '🐢' or g[2] == g[4] == g[6] == '🐢')
while True:
    x=int(input("X= "))
    while g[x-1]=='🐍' or g[x-1]=='🐢':
        print("Bu joy band qaytarib kriing >>>>>>>>>>>")
        x=int(input("X= "))
    g[x-1] = '🐍'
    jadval()

    if g[0]==g[1]==g[2]=='🐍' or g[3]==g[4]==g[5]=='🐍' or  g[6]==g[7]==g[8]=='🐍' or \
            g[0]==g[3]==g[6]=='🐍' or g[1]==g[4]==g[7]=='🐍' or  g[2]==g[5]==g[8]=='🐍' or g[0]==g[4]==g[8]=='🐍' or  g[0]==g[4]==g[8]=='🐍' or  g[2]==g[4]==g[6]=='🐍':
        print("🐍 yuti tamom!!!!")
        break
    y = int(input("Y= "))
    while g[y - 1] == '🐍' or g[y - 1] == '🐢':
        print("Bu joy band qaytarib kriting >>>>>>>>>>>")
        y=int(input("Y= "))
    g[y - 1] = '🐢'
    jadval()
    if :
        print("🐢 yuti tamom!!!!")
        break
        