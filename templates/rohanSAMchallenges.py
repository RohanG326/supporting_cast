from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json


def swap(age1, age2):
    a = age1
    b = age2
    if a <= b:
        return a, b
    else:
        return b, a

matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
def formatting():
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            print(matrix[x][y], end=" ")
        print()

        # for a in range(len(matrix[1])):
        #     print(a)


# if __name__ == "__main__":
#     input1 = input("first age")
#     input2 = input("second age")
#     a, b = swap(input1, input2)
#     print(a, b)


if __name__ == "__main__":
    formatting()

