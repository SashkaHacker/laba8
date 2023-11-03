#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 11

if __name__ == "__main__":
    print("Введите количество очков через пробел")
    tupl = tuple(map(lambda x: int(x), input().split()))
    iterab = tupl[0]
    flag = False
    for i in tupl[1:]:
        if i > iterab:
            flag = True
            break
        iterab = i
    if flag:
        print("В списке команды расположены неправильно")
    else:
        print("В списке команды расположены правильно")
