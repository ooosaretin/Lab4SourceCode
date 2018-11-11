# -*- coding: utf-8 -*-
"""
Course: CS 2302
Author: Wenro Osaretin
Instructor: Diego Aguirre
T.A.: Anindita Nath
Date of Last Modication: November 11, 2018
"""
#This is where I insert the english words in the hash table
# and then preform some operations to solve collisions
class HNode:
    #This is the node class that I will use for the Hash Table
    def __init__(self, words, next):
        self.key = words
        self.next = next

class HT:
    #This is where I use the node class for the initialization
    #of the Hash Table since the Hash Table is an array of linked list
    def __init__(self, quantity):
        self.HTable = [None] * quantity
    #This is where I took the module of the key I inserted with the table size
    # but this time I also converted the letters in the words to integer by
    #taking the sum of the letters in each words
    def hash(self, k):
        s = 0
        for i in range(len(k)):
            s = s + ord(k[i])
        return s % len(self.HTable)
    
    #This is where I insert the key in the table by positioning it and then
    #creating a linked list out of the key
    def insert(self, k):
        pos = hash(k)
        self.HTable[pos] = HNode(k, self.HTable[pos])
        
    #This is where I search for a key in the table
    def search(self, k):
        pos =  hash(k)
        temp = self.HTable[pos]
        while temp != None and temp.key != k:
            temp = temp.next
        return temp
    
    #This is where I find the the average numbers of comparisons
    def average_compare(self, k):
        count = 0
        pos =  hash(k)
        for i in self.HTable:
            temp = self.HTable[pos]
            while temp != None:
                if temp.key == k:
                    count = count + 1
                temp = temp.next
            return count / len(self.HTable)
        
    #This is where I compute the load factor of which I have to divide the 
    # number of elements by the size of the table
    def load_factor(self, k):
        counter = 0
        pos = hash(k)
        for i in self.HTable:
            temp = self.HTable[pos]
            while temp != None:
                counter = counter+1
                temp = temp.next
            return counter / len(self.HTable)
    

#This is where I display my results            
file = open("words.txt")
lines = file.readline()
file.close()
for i in lines:
    h = HT(350000)
    num = h.hash(i)
    print(num)
    print("--------------")
    print("Insertion: ")
    print(h.insert(num))
    print("--------------")
    print("Search for 2:")
    print(h.search(2))
    print("--------------")
    print("Average Numbers of Comparison: ")
    print(h.average_compare(num))
    print("--------------")
    print("The load factor: ")
    print(h.load_factor(num))
    print("--------------------------")
    print("--------------------------")
    