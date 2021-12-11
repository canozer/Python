
def selectedFood():
    with open("FoodList.txt", "r") as FILE:
        for YEMEK in FILE:
            print(YEMEK)


def foodName():
    ad = input("Food Name: ")
    with open("FoodList.txt", "a") as FILE:
        FILE.write("Yemeğin Adı :" + " " + ad + '\n')




def writeMaterial():
    malzeme = input('Material Name: ')

    with open("FoodList.txt", "a") as FILE:
        FILE.write("Malzemeler : " + " " + malzeme + '\n')




while True:
    Food = input('1- Selected Food \n 2- Food Name Enter \n 3-Write Material  \n 4- Exit\n')

    if Food == '1':
        selectedFood()
    elif Food == '2':
        foodName()
    elif Food == '3':
        writeMaterial()
    else:
        break

