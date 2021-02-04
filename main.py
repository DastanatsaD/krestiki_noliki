crossOrZero = 1
numbers = {
    "n1": " ",
    "n2": " ",
    "n3": " ",
    "n4": " ",
    "n5": " ",
    "n6": " ",
    "n7": " ",
    "n8": " ",
    "n9": " "
}
print('       Старт!')
print(' ----- ----- -----')
print('|     |     |     |')
print(' ----- ----- -----')
print('|     |     |     |')
print(' ----- ----- -----')
print('|     |     |     |')
print(' ----- ----- -----')

while True:
    try:
        xOr0 = "X"
        if crossOrZero % 2 == 0:
            xOr0 = "O"
        else:
            xOr0 = "X"

        number = int(input(f"Введите номер от 1 до 9 вы {xOr0}: "))

        if number > 9:
            raise TypeError
        else:
            if numbers["n" + str(number)] == " ":
                crossOrZero += 1
                if crossOrZero % 2 == 0:
                    numbers["n" + str(number)] = "X"
                else:
                    numbers["n" + str(number)] = "O"
            else:
                print("Ход занят!")

            print('  ----- ----- -----')
            print(f'|  {numbers["n1"]}  |  {numbers["n2"]}  |  {numbers["n3"]}  |')
            print(f' ----- ----- -----')
            print(f'|  {numbers["n4"]}  |  {numbers["n5"]}  |  {numbers["n6"]}  |')
            print(f' ----- ----- -----')
            print(f'|  {numbers["n7"]}  |  {numbers["n8"]}  |  {numbers["n9"]}  |')
            print(f' ----- ----- -----')

            if numbers["n1"] == "O" and numbers["n2"] == "O" and numbers["n3"] == "O":
                print("Победил O!")
                break
            elif numbers["n4"] == "O" and numbers["n5"] == "O" and numbers["n6"] == "O":
                print("Победил O!")
                break
            elif numbers["n7"] == "O" and numbers["n8"] == "O" and numbers["n9"] == "0":
                print("Победил O!")
                break
            elif numbers["n1"] == "O" and numbers["n4"] == "O" and numbers["n7"] == "O":
                print("Победил O!")
                break
            elif numbers["n2"] == "0" and numbers["n5"] == "O" and numbers["n8"] == "O":
                print("Победил O!")
                break
            elif numbers["n3"] == "O" and numbers["n6"] == "O" and numbers["n9"] == "O":
                print("Победил O!")
                break
            elif numbers["n1"] == "O" and numbers["n5"] == "O" and numbers["n9"] == "O":
                print("Победил O!")
                break
            elif numbers["n3"] == "O" and numbers["n5"] == "O" and numbers["n7"] == "O":
                print("Победил O!")
                break

            elif numbers["n1"] == "X" and numbers["n2"] == "X" and numbers["n3"] == "X":
                print("Победил X!")
                break
            elif numbers["n4"] == "X" and numbers["n5"] == "X" and numbers["n6"] == "X":
                print("Победил X!")
                break
            elif numbers["n7"] == "X" and numbers["n8"] == "X" and numbers["n9"] == "X":
                print("Победил X!")
                break
            elif numbers["n1"] == "X" and numbers["n4"] == "X" and numbers["n7"] == "X":
                print("Победил X!")
                break
            elif numbers["n2"] == "X" and numbers["n5"] == "X" and numbers["n8"] == "X":
                print("Победил X!")
                break
            elif numbers["n3"] == "X" and numbers["n6"] == "X" and numbers["n9"] == "X":
                print("Победил X!")
                break
            elif numbers["n1"] == "X" and numbers["n5"] == "X" and numbers["n9"] == "X":
                print("Победил X!")
                break
            elif numbers["n3"] == "X" and numbers["n5"] == "X" and numbers["n7"] == "X":
                print("Победил X!")
                break

            if numbers["n1"] != " " and numbers["n2"] != " " and numbers["n3"] != " " and numbers["n4"] != " " and numbers["n5"] != " " and numbers["n6"] != " " and numbers["n7"] != " " and numbers["n8"] != " " and numbers["n9"] != " ":
                print("Ничья!")
                break
    except ValueError:
        print("Введите ЦИФРУ, а не букву!")
    except TypeError:
        print("Введите цифру меньше 9!")
    except KeyError:
        print("Введите цифру больше 0!")
