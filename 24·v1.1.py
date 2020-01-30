#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Li Baoyan'

# @Create Time:   2019-10-02 09:58:59
# @Last Modified Time: 2019-10-06 12:10:33

# 增加了输入检查


def input_check_errow(b, a):
    '''input的加强版，输入提示内容和试错语句（string），对用户引发错误的输入进行拦截，直到合法才放行。'''
    global inp, inp1
    inp = input(b)
    inp1 = inp
    while True:
        try:
            exec(a)
            break
        except:
            print("输入不合法，请重新输入.")
            inp = input(b)
            inp1 = inp
    return inp1


while True:
    a = input_check_errow('Num.1:', 'inp=int(inp)')
    b = input_check_errow('Num.2:', 'inp=int(inp)')
    c = input_check_errow('Num.3:', 'inp=int(inp)')
    d = input_check_errow('Num.4:', 'inp=int(inp)')
    operlist = ['+', '-', '*', '/']
    unrep = [1, 2, 3, 4]
    alist = []
    numalist = []
    operalist = []
    finalist = []
    list24 = []
    repdic = {1: str(a), 2: str(b), 3: str(c), 4: str(d)}
    for i in unrep:
        for j in unrep:
            for k in unrep:
                for l in unrep:
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        alist.append([i, j, k, l])
    for i in alist:
        k = [repdic[j] for j in i]
        numalist.append(k)
    for i in operlist:
        for j in operlist:
            for k in operlist:
                operalist.append([i, j, k])
    for i in numalist:
        for j in operalist:
            finalist.append(
                '(' + '(' + i[0] + j[0] + i[1] + ')' + j[1] + i[2] + ')' + j[2] + i[3])
            finalist.append('(' + i[0] + j[0] + i[1] + ')' +
                            j[1] + '(' + i[2] + j[2] + i[3] + ')')
            finalist.append(
                '(' + i[0] + j[0] + '(' + i[1] + j[1] + i[2] + ')' + ')' + j[2] + i[3])
            finalist.append(
                i[0] + j[0] + '(' + '(' + i[1] + j[1] + i[2] + ')' + j[2] + i[3] + ')')
            finalist.append(i[0] + j[0] + '(' + i[1] + j[1] +
                            '(' + i[2] + j[2] + i[3] + ')' + ')')
    for i in finalist:
        try:
            if eval(i) == 24:
                list24.append(i)
        except ZeroDivisionError:
            pass
    print(str(len(list24)) + ' Ways:')
    for i in list24:
        print(i)
    print('Fin.')
