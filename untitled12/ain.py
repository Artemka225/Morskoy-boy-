def ships_add(n):
    print("Расположите ваши корабли")
    for i in range(1, 5):
        n=ships_info(n, i)
    return n

def ships_info(n, lenship):
    z1 = list(map(int, input("Выберите где будет распологаться первая клетка"+ lenship +"- х палубного корабля").split()))
    z2 = list(map(int, input("Выберите где будет распологаться последняя клетка"+ lenship+"- х палубного корабля").split()))
    print(z1, z2)
    if (z2[0] - z1[0] == lenship-1):
        for i in range(z1[0] - 1, z2[0]):
            n[z1[1]][i] = 1
    elif (z2[1] - z1[1] == lenship-1):
        for i in range(z1[1] - 1, z2[1]):
            n[i][z1[1]] = 1
    else:
        print("ведены не корректные значения")
    return n

def print_plase(n):
    for i in range(10):
        print(n[i])

def frame_ships(n, z1, z2):
    if (z1[0]-1>0)and(z1[0]+1<11):
        if (z1[1]-1>0)and(z1[1]+1<11):
            for i in range(z1[0]-2,z2[0]+1):
                n[i][z1[1]]=0
            for i in range()

def main():
    n=[[[] for i in range(10)] for j in range(10)]
    m=[[[] for i in range(10)] for j in range(10)]
    print_plase(n)
    print_plase(m)
    n=ships_add(n)
    print_plase(n)
if __name__=='__main__':
    main()
