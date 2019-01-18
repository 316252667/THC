# -*- coding: utf-8 -*-
S='_|?|_|?|_|?|_|?|_|?|_|?|_|?|'
C = -20
iC = 5
while C <= 40:
    F = (9.0/5)*C +32
    print C, F
    C= C + iC
'''
l = [1,3,6,45]
while bool (l):
    l.pop() 
print (l)
'''
print S
gradosC = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print '    C    F'
for grado in gradosC:
    F = (9.0/5)*grado + 32
    print '%5d %5.lf' % (grado, F)
print S
indice = 0
print '    C    F'
while indice <len(gradosC):
    C = gradosC[indice]
    F = (9.0/5)*C + 32
    #print C, F
    print '%5d %5.1f' % (C, F)
    indice+=1
print S

gradosC = []
for C in range(-20,45,5):
    gradosC.append(C)
print gradosC

print S
gradosC = []
for i in range(0,21):
    C = -20 + i*2.5
    gradosC.append(C)
print gradosC
L=[-20]
while L[len(L)-1]!= 30:
    L.append(L[len(L)-1]+2.5)
    
