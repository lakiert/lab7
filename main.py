import numpy as np

# zad 1
# a = np.array([2,4,6])
# b = np.array([1,2,3])
# print(a)
# print(b)
# c = a*b
# print(c)


# zad 2
# a = np.arange(9).reshape(3, 3)
# b = np.arange(16).reshape(4, 4)
# print(a)
# print('minimalne wartosci rzedow: %s'% (a.min(axis=1)))
# print('minimalne wartosci kolumn: %s'% (a.min(axis=0)))
# print(b)
# print('minimalne wartosci rzedow: %s'% (b.min(axis=1)))
# print('minimalne wartosci kolumn: %s'% (b.min(axis=0)))


# zad3
# a = np.array([2,4,6])
# b = np.array([1,2,3])
# print(np.dot(a,b))


# zad4
# a = np.array([1,2,3])
# b = np.array([2.5, 1.5, 0.5])
# c = a*b
# print(c)


# zad5
# import math as math
# macierz = np.arange(6).reshape(2,3)
# print(macierz)
# for x in range(2):
#     for y in range(3):
#         a = math.sin(macierz[x,y])
#         print(a)


# zad6
# import math as math
# macierz = np.arange(6).reshape(2,3)
# print(macierz)
# for x in range(2):
#     for y in range(3):
#         b = math.cos(macierz[x,y])
#         print(b)


# zad7
# a = np.array([1, 2, 3, 4]).reshape(2, 2)
# b = np.array([2, 4, 1, 5]).reshape(2, 2)
# c = a+b
# print(c)


# zad8
# a = np.arange(9).reshape(3, 3)
# print(a)
# for x in range(3):
#     print(a[x, :])


# zad9
# a = np.arange(9).reshape(3, 3)
# print(a)
# for b in a.flat:
#     print(b)
#     print("")


# zad10
# a = np.arange(9*9).reshape(9, 9)
# print(a)
# print(a.reshape(1, 81))
# print(" ")
# print(a.reshape(3, 27))
# print(" ")
# print(a.reshape(27, 3))
# print(" ")
# print(a.reshape(81, 1))

# mozliwosci zmiany ksztaltu macierzy zaleza
# od dzielnikow liczby, ktora jest liczba wszystkich
# elementow tej macierzy


# zad11
# a = np.arange(12).reshape(3, 4)
# b = np.arange(12).reshape(4, 3)
# c = np.arange(12).reshape(2, 6)
#
# print(a)
# print("")
# print(b)
# print("")
# print(c)
# print("")
# print(a.ravel())
# print(b.ravel())
# print(c.ravel())
