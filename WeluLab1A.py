#!/usr/bin/env python3

import math


class Rectangle:

    def __init__(self, length, width):
##        if length < 0:
##            length = 1
##        if width < 0:
##            width = 1
##        self.__length = length;
##        self.__width = width;
        self.setLength(length)
        self.setWidth(width)

    def getLength(self):
        return self.__length

    def setLength(self, length):
        if length < 0:
            length = 1
        self.__length = length

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if width < 0:
            width = 1
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return ((self.__length * 2) + (self.__width * 2)) 

def main():
    print("*****************************************")
    print("Welcome to the Rectangle Object Program")
    print("-----------------------------------------")
    print("You will be creating a Rectangle Object")
    print("-----------------------------------------")
    print("Then the Object details will be displayed")
    print("*****************************************")
    print()
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    c = Rectangle(a, b)
    print()
    print("=== Rectagle ===")
    print("Length:", c.getLength())
    print("Width:", c.getWidth())
    print("Area:", c.getArea())
    print("Perimeter:", c.getPerimeter())
    print()

main() 
