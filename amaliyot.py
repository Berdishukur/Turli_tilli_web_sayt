
g=['*','*','*','*','*','*','*','*','*']
print(f"""
| {g[0]} | {g[1]} | {g[2]} |
| {g[3]} | {g[4]} | {g[5]} |
| {g[6]} | {g[7]} | {g[8]} |
""")
while True:
    x = int(input("X= "))
    while g[x-1]=='X' or g[x-1]=='Y':
        print("Bu joy band qaytadan kiriting>>>>")
        x = int(input("X= "))
    g[x - 1] = 'X'
    print(f"""
    | {g[0]} | {g[1]} | {g[2]} |
    | {g[3]} | {g[4]} | {g[5]} |
    | {g[6]} | {g[7]} | {g[8]} |
    """)
    if g[0]==g[1]==g[2]=='X' or g[3]==g[4]==g[5]=='X' or g[6]==g[7]==g[8]=='X' or \
            g[0]==g[3]==g[6]=='X' or g[1]==g[4]==g[7] =='X' or g[2]==g[5]==g[8] =='X' or g[0]==g[4]==g[8]=='X' or g[2]==g[4]==g[6]=='X':
        print(" X yutdi , Tamom!!! ")
        break