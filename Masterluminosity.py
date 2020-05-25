import matplotlib.pyplot as plt
import numpy as np
import pylab
import matplotlib.lines as lines

lum = []
days= []
with open('2014dtlum.csv') as f:
     for row in f.readlines():
        row.strip('\n')
        if not row.startswith("#"):
            spaces=row.split(',')
            lum.append(float(spaces[0]))
            days.append(float(spaces[1]))

lumdt = []
daysdt= []
with open('Knowniaxlum.csv') as f:
     for row in f.readlines():
        row.strip('\n')
        if not row.startswith("#"):
            spacesdt=row.split(',')
            lumdt.append(float(spacesdt[0]))
            daysdt.append(float(spacesdt[1]))

lumIa = []
daysIa= []
with open('Ialum_fromplot.csv') as f:
     for row in f.readlines():
        row.strip('\n')
        if not row.startswith("#"):
            spacesIa=row.split(',')
            lumIa.append(float(spacesIa[0]))
            daysIa.append(float(spacesIa[1]))


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pylab


#Iax

#08A
x1=[daysdt[1],daysdt[1]]
y1=[lumdt[1],lumdt[1]*.6]
plt.scatter(daysdt[1],lumdt[1],color='red',s=50,label='1.51 - 8.5 GHz, Type Iax')
plt.errorbar(x1,y1,uplims=True,yerr=.5,color='red')


#05hk
x2=[daysdt[0],daysdt[0]]
y2=[lumdt[0],lumdt[0]*.6]
plt.scatter(daysdt[0],lumdt[0],color='red',s=50)
plt.errorbar(x2,y2,uplims=True,yerr=.5,color='red')
#

#2012z
x3=[daysdt[2],daysdt[2]]
y3=[lumdt[2],lumdt[2]*.6]
plt.scatter(daysdt[2],lumdt[2],color='red',s=50,zorder=2)
plt.errorbar(x3,y3,uplims=True,yerr=.5,color='red')

#08ha
x4=[daysdt[3],daysdt[3]]
y4=[lumdt[3],lumdt[3]*.6]
plt.scatter(daysdt[3],lumdt[3],color='red',s=50)
plt.errorbar(x4,y4,uplims=True,yerr=.5,color='red')



#SN2019muj
#frequency 5.08 GHz

mx=[11,11]
my=[7.64E25,7.64E25*.6]
plt.scatter(mx[0],my[0],color='red',s=50)
plt.errorbar(mx,my,uplims=True,yerr=.5,color='red')

#frequency 1.51GHz
mx1=[13,13]
my1=[1.00E26,1.00E26*.6]
plt.scatter(mx1[0],my1[0],color='red',s=50)
plt.errorbar(mx1,my1,uplims=True,yerr=.5,color='red')

plt.plot([mx[0],mx1[0]],[my[0],my1[0]],'k-',lw=5,alpha=.5,color='red')


###################################################################

#2014dt 12.3

#28 days
x4=[28,28]
y4=[lum[1],lum[1]*.6]
plt.scatter(28,lum[1],color='red',marker="*",s=200, zorder=3,edgecolor='black')
plt.errorbar(x4,y4,uplims=True,yerr=.5,color='red',marker="")

#38 days
x4a=[38,38]
y4a=[lum[1],lum[1]*.6]
plt.scatter(38,lum[1],color='red',marker="*",s=200, zorder=3,edgecolor='black')
plt.errorbar(x4a,y4a,uplims=True,yerr=.5,color='red',marker="")

plt.errorbar(33,10e+24,uplims=True,xerr=5,color='red',marker="")


#2014dt 19.3

#28 days
x4=[28,28]
y4=[lum[0],lum[0]*.3]
plt.scatter(28,lum[0],color='red',marker="*",s=200, zorder=3,edgecolor='black')
plt.errorbar(x4,y4,uplims=False,yerr=.01,color='red',marker="")

#38 days
x4a=[38,38]
y4a=[lum[0],lum[0]*.3]
plt.scatter(38,lum[0],color='red',marker="*",s=200, zorder=3,edgecolor='black')
plt.errorbar(x4a,y4a,uplims=False,yerr=.01,color='red',marker="")

plt.errorbar(33,23e+24,uplims=True,xerr=5,color='red',marker="")


###################################################################
#plot ias
def plotia(which):
    time = [daysIa[which],daysIa[which]]
    lum =[lumIa[which],lumIa[which]*.6]
    plt.scatter(time[0],lum[0],color='blue', s=50,zorder=0)
    plt.errorbar(time,lum,uplims=True,yerr=.5,color='blue')

#just for the ia label
plt.scatter(daysIa[0],lumIa[0],color='blue',s=50,zorder=0,label='5.9 - 7.4 GHz, Type Ia')

for i in range(0,23):
    plotia(i)

def connecting_line(which):
    plt.plot([daysIa[which],daysIa[which+1]],[lumIa[which],lumIa[which+1]],'k-',lw=5,alpha=.5,color='blue',zorder=0)

#connecting 11fe points
connecting_line(0)
connecting_line(1)
connecting_line(2)
connecting_line(3)
connecting_line(4)

#connecting 14jpoints
connecting_line(6)
connecting_line(7)
connecting_line(8)

#connectiing 10iuv
connecting_line(10)

#connecting line 14ag
connecting_line(13)

#connnecitng 11by
connecting_line(13)
connecting_line(14)

#connecting line 12cg
connecting_line(16)
connecting_line(17)
connecting_line(18)
connecting_line(19)

#connecting line 12ht
connecting_line(21)

#############################################################################
plt.xlim(1.5,400)
plt.ylim(1e23,6e27)
plt.yscale('log')
plt.xscale('log')

plt.scatter(28,lum[1],color='red',marker="*",s=200, label='7.4  GHz, SN$\,$2014dt',zorder=0)

leg = plt.legend(loc='upper left',frameon=False,prop={'size': 10});

plt.tick_params(direction='out', length=6, width=1,right='on', top='on', which='both')

plt.text(2,1.5e24, '2011fe',fontsize=12,color='blue')
plt.text(25,5e23, '2014J',fontsize=12,color='blue')

plt.text(1.7*days[1], 2*lum[1], '2014dt',fontsize=12,color='red',)
plt.text(8,1e25, '2012Z',fontsize=12,color='red')
plt.text(4.6,1e26,'2019muj',fontsize=12,color='red')






plt.xlabel('Time Since Explosion (Days)', fontsize=12)
plt.ylabel('Luminosity Density $(erg \ s^{-1} \ Hz^{-1})$', fontsize=12)
#
plt.savefig('Radiosample.pdf',format='pdf')
plt.show()
