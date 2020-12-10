# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:50:44 2020

@author: d.jung
"""
#Based on Numpy



from numpy import matrix 
from numpy import shape


def laff_copy(x,y):
    assert type(x) == matrix and len(x.shape) == 2
    assert type(y) == matrix and len(y.shape) == 2
    
    m_x, n_x = shape (x)
    m_y, n_y = shape (y)
    
    assert m_x == 1 or n_x == 1, "laff_copy: x is not a vector"
    assert m_y == 1 or n_y == 1, "laff_copy: y is not a vector"
    assert m_x == m_y and n_x == n_y, "laff_copy: vectors are of different size"

    
    if m_x != 1:
        for i in range(m_x):
            y[i,0] = x[i,0]
    if n_x != 1:
        for j in range(n_x):
            y[0,j] = x[0,j]
    





def laff_scal(x, n):
    #Assert input type
    assert type(x) == matrix, "laff_scal: input x is not ok"
    assert type(n) in (int, float), "laff_scal: input n is not a numeric value"
    
    
    #Assert vector by shape
    m_x, n_x = shape(x)
    assert m_x == 1 or n_x == 1, "laff_scal: input is not vector"

    
    if m_x != 1: 
        for i in range(m_x):
            x[i,0] = x[i,0] * n
    
    elif n_x != 1:
        for j in range(n_x):
            x[0,j] = x[0,j] * n


def laff_axpy(alpha,x,y):
    assert type(alpha) in (int, float), "laff_axpy: alpha is not numerical"
    assert type(x) == type(y) == matrix, "laff_axpy: x or y is not of type matrix"
    
    m_x, n_x = shape(x)
    m_y, n_y = shape(y)
    
    assert min(m_x, n_x) == min(m_y, n_y) == 1, "laff_axpy: Either x or y not a vector"
    assert max(m_x, n_x) == max(m_y, n_y), "laff_axpy: Vectors are not of same size"
    
    if m_x != 1:
        for i in range (m_x):
            x[i,0] = x[i,0] * alpha, + y[i,0] 
        

    elif n_x != 1:
        for j in range (n_x):
            x[0,j] = x[0,j] * alpha + y[0,j]

    
        












######
    
xvec = matrix([2,3,4])
yvec = matrix([None, None, None])

xcol = matrix([[2],[3],[4]])
ycol = matrix([[None],[None],[None]])