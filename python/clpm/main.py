__author__ = 'foury'
import cv2
import numpy as np
import matplotlib as plt
import read_csv
import numpy.linalg as LA
from numpy.linalg import inv


#read picture in a list
L=read_csv.readCSV("/Users/foury/Documents/github/amygit/FR/FR_SR/FR_SR/testimg2/high/low_downsampled/low_d.csv")
H=read_csv.readCSV("/Users/foury/Documents/github/amygit/FR/FR_SR/FR_SR/testimg2/high/high_downsampled/high_d.csv")
#calculate delta
M=H[0].size#i add the first change here
m=L[0].size
print M,m
Nt=len(H)
W= np.zeros([len(H),len(H)])
inner_sum=0

for i in range(0,len(H)):

    for j in range(0,len(H)):

        k=i+1
        if k >len(H)-1:
            k=i-1
        inner= np.sum((H[int(i)]-H[int(k)])**2)
        inner_2=np.sum((H[int(i)]-H[int(j)])**2)
        inner_sum=inner_sum+inner_2
delta=inner_sum/Nt**2

#calculate Wij
for i in range(0,len(H)):

    for j in range(0,len(H)):

        k=i+1
        if k >len(H)-1:
            k=i-1
        inner= np.sum((H[int(i)]-H[int(k)])**2)
        W[i,j]=np.exp(-1*inner/delta**2)
W=np.array(W)

#calculate D
D_l = np.zeros([len(H),len(H)])
D_h = np.zeros([len(H),len(H)])

for i in range(0,len(H)):

        D_l[i,i]=np.sum(W[i])
        D_h[i,i]=np.sum(W.transpose()[i])

#define A
D_l=np.array(D_l)
D_h=np.array(D_h)
A_ud1=[]
A_ud2=[]
A=[]
A_ud1=np.concatenate((D_l,-1*W.transpose()),axis=0)
A_ud2=np.concatenate((D_l,-1*W),axis=0)
A=np.concatenate((A_ud1,A_ud2),axis=1)

#define Z
L_r=[]
H_r=[]
for i in range(0,len(L)):
    L_temp=np.reshape(L[i],[1,L[0].size])
    L_r.append(L_temp)
    H_temp=np.reshape(H[i],[1,H[0].size])
    H_r.append(H_temp)
print "this is",L_r[0].size
L_rr=np.reshape(L_r,[len(L),L_r[0].size])
L_rr=np.transpose(L_rr)
H_rr=np.reshape(H_r,[len(H),H_r[0].size])
H_rr=np.transpose(H_rr)
#L_r=np.array(L_r)
#H_r=np.array(H_r)


Z=np.zeros([m+M,2*Nt])
print "look at this",Z.shape
print m,Nt
print "that is",Z[m:m+M,Nt:Nt*2].shape

Z[0:m,0:Nt]=L_rr#should transfer to colum
Z[m:m+M,Nt:2*Nt]=H_rr#find problems
print Z.shape
print A.shape
#define E F
Z_t=np.transpose(Z)
E=np.dot(np.dot(Z,A),Z_t)
F=np.dot(Z,Z_t)
F_inv=inv(F)
G=np.dot(F_inv,E)
print G
#calculate 2-d+1 smallest generalized eigenvectors

w,v=LA.eig(G)
#pickup the 2-nd to d+1st smalles
for j in range(0,len(w)):
    print w[j]






