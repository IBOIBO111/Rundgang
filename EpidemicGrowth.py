import matplotlib.pyplot as plt
import numpy as npy

def SIR_Step(_alpha,_beta,_sir,_dt):
    #_sir ist ein Tupel [S,I,R]
    total = sum(_sir)
    sep = _sir[0]-_alpha*_sir[0]*_sir[1]*_dt
    rec = _sir[2]+_beta*_sir[1]*_dt
    inf = _sir[1]+_sir[1]*(_alpha*_sir[0]-_beta)*_dt
    _sir = [sep,inf,rec]
    return _sir


Population = 76.0E6   #Bevölkerung
#Population = 80.0E6


#Infected
I = 195.0            #Startwert der Infizierten
I_ = []
#Regenerated
R = 30.0               # Genesene
R_ = []
#Susceptible
S = Population-I-R      #Startwert
S_ = []
#Timestep
dt = 0.1            #day
#WÜbertragungsrate
#alpha = 1.78E-9      #1/Day*1/People
alpha = 3.0E-9
# Genesungsrate
beta = 1.0/14.0     #People/day

#Basis Reproduktionsrate
R0 = Population*alpha/beta
print(R0)

#RKI Daten
RKI_t = [30.0, 31.0,  32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0]
RKI =   [60000,61800,68500,74700,85640,89650,92540,96790,98940]



#EndTime
EndTime = 40      #days

t=npy.arange(0.0,EndTime,dt)

#Exponentiell
expon=I*npy.exp(alpha*Population*t)

SIR = [S,I,R]
for ttime in t:
    SIR = SIR_Step(alpha,beta,SIR,dt)
    S_.append(SIR[0])
    I_.append(SIR[1])
    R_.append(SIR[2])


#plt.plot(t,S_,'r+',t,I_,'bo',linewidth=2)
#plt.plot(t,expon,RKI_t,RKI,'ob',linewidth=2)
plt.plot(t,I_,RKI_t,RKI,'ob',linewidth=2)
plt.xlabel('Zeit [s]')
plt.ylabel('y(t)')
plt.title('Diagrammüberschrift')
plt.grid(True)
plt.show()



