# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:08:45 2021

@author: Lukas
Source : André Warusfel
"""
from tkinter import *
from random import randint
from sympy import nextprime
    
def bezout_fct(a:int,b:int)->int:
    if b == 0:
        return 1,0
    else:
        u , v = bezout_fct(b , a % b)
        return v , u - (a//b)*v
    
def resoud_equation(a,b,c):
    u,v = bezout_fct(a,b)
    return u+b

def conv(txt): 
    r=[]
    for i in txt:
        r.append(ord(i))
    return r

def reverse(liste): 
    print('message déchiffré : ' + str(liste))
    r=''
    for i in liste:
        r=r+chr(i)
    return r

def chiffrement(texte): 
    a=conv(texte)
    N, e, d , p = gen_cle2()
    for i in range(len(a)):
        a[i]=suite_de_lucas(e,a[i],N)
    return a, N, d

def dechiffrement(liste,N,d):
    for i in range(len(liste)):
        liste[i]=suite_de_lucas(d,liste[i],N)
    liste=reverse(liste)
    return liste

def chiffre_puis_dechiffre(texte): 
    a,N,d=chiffrement(texte)
    print('message chiffré : ' + str(a))
    rep=dechiffrement(a, N, d)
    return rep

    
def table2(a,b,c): 
    i=1
    d=a%c
    while d!=1:
        d=(d*a)%c
        i+=1
    e=b%i
    if e==0:
        return 1
    else :
        return (a**e)%c

def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def ppcm(*n):
    def _pgcd(a,b):
        while b: a,b = b, a%b
        return a 
    p=abs(n[0]*n[1])//_pgcd(n[0],n[1])
    for x in n[2:]:
        p=abs(p*x)//_pgcd(p,x)
    return p
    
a5,b5=20,50

def gen_cle2():
    global a5,b5
    pi=nextprime(randint(a5, b5))
    omega=nextprime(randint(a5, b5))
    while pi==omega:
        pi=nextprime(randint(a5, b5))
        omega=nextprime(randint(a5, b5))       
    p=3
    N=pi*omega
    print(N)
    a1=(pi-1)*(omega-1)
    a2=(pi+1)*(omega-1)
    a3=(pi-1)*(omega+1)
    a4=(pi+1)*(omega+1)
    r=ppcm(a1,a2,a3,a4)
    e=randint(a5,b5)
    while pgcd(e,r)!=1:
        e=randint(a5,b5)
    d=resoud_equation(e, r, 1)
    assert (d*e)%r==1
    return N,e,d,p

def suite_de_lucas(e,p,N):
    liste={0:2,1:p}
    for i in range(e+1):
        if i not in liste.keys():
            liste[i]=(p*liste[i-1]-liste[i-2])%N
        if i>3:
            del liste[i-3]
    return liste[e]%N





  