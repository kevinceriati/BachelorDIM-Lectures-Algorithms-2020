# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

bases syntaxique de Python:

a=1
b='e'+str(a)

if a==1:
    c=3
    d=4
    
#Basic loop
for i in range(4):
    print('i')
    

def my_addition(a,b):
  
            This function adds two numbers
            Args:
                a: the first number
                b: the second number
            Returns the sum of the two
   
    return a+b
"""

#SESSION 1
"""
Algorithm 1 Selective average

What happens if Som initialization is forgotten ?
=> Un crash car somme non initialisé

• What can you expect if all the values are below zero ?
=> Il faut catch l'exeption suivant si la valeur est positive ou négative

• Translate this algorithm in the python3.x language within script of name
S1_algotools.py. You must implement this algorithm as a function that
follows prototype "function average_above_zero(table:list) returns float".

• Commit the code to your local repository and push to your GitHub repository.
"""

def average_by_zero(l_in):
    '''
    this function does an average of positive value
    
    Parameters:
        liste_in : the input list
        
    Return : the average
    '''

    mysum = 0
    positive_element_count=0
    for element in l_in:
        if element>0:
            mysum+=element
            '''mysum=som+element'''
            positive_element_count+=1
    if positive_element_count>0:
        average=mysum/positive_element_count
    else:
        raise ValueError('no positive value !')
    return average
    
my_list=[0,2,-3]
average=average_by_zero(my_list)
print('My average' , average)                       
