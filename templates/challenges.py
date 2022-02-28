from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json
import random as rand


def swapper(int1, int2):
    print(int1, int2)
    if int1 >= int2:
        x1 = int1
        int1 = int2
        int2 = x1

    return int1, int2

def matrix1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    print("Swap Function")
    userinput1 = input("Enter a number")
    userinput2 = input("Enter another number")
    x, y = swapper(userinput1, userinput2)
    print(x, y)
    print("Printing Matrix")
    matrix1()




