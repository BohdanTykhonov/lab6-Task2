def find_surrounding_elements(user_list, target):
    if target in user_list:
        index = user_list.index(target)

        if index == 0:
            print("Заданий елемент знаходиться на початку списку, сусіда ліворуч немає.")
            print(f"Елемент праворуч: {user_list[index + 1]}")
        elif index == len(user_list) - 1:
            print("Заданий елемент знаходиться в кінці списку, сусіда праворуч немає.")
            print(f"Елемент ліворуч: {user_list[index - 1]}")
        else:
            print(f"Елемент ліворуч: {user_list[index - 1]}")
            print(f"Елемент праворуч: {user_list[index + 1]}")
    else:
        print("Заданий елемент відсутній у списку.")

user_input = input("Введіть елементи списку через пробіл: ")
user_list = [int(x) for x in user_input.split()]
target = int(input("Введіть елемент, для якого потрібно знайти сусідні елементи: "))

find_surrounding_elements(user_list, target)
