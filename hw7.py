# File: hw7.py
# Student: Preston Cook
# UT EID: plc886
# Course: CS303E
# 
# Date: 12/16/2022
# Description of Program: Basic OOP to create student class

class Student:
    def __init__(self, name, exam1=None, exam2=None):
        self.__name = name
        self._exam1 = exam1
        self._exam2 = exam2
    
    def getName(self):
        return self.__name
    
    def getExam1Grade(self):
        return self._exam1
    
    def setExam1Grade(self, grade):
        self._exam1 = grade
    
    def getExam2Grade(self):
        return self._exam2
    
    def setExam2Grade(self, grade):
        self._exam2 = grade
    
    def getAverage(self):
        g1, g2 = self._exam1, self._exam2
        if not g1 or not g2:
            print('Some exam grades are not available.')
        else:
            return round((g1 + g2) / 2, 2)

    def __str__(self):
        return f'Student: {self.__name}\n  Exam1: {self._exam1}\n  Exam2: {self._exam2}'