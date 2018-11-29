import matplotlib.pyplot as plt
import matplotlib
from TempLib import *
import numpy as np
git remote add origin https://github.com/pallepop/Balloon-Internal-Temperature-Simulation.git
git push -u origin master

#*****************************************
thicknessLimitUp=0.08
thicknessLimitDown=0.02
thicknessDividers=(thicknessLimitUp-thicknessLimitDown)/10
#*****************************************

initialAltitude = 0 #In m
maxAltitude = 26000 #In m
#maximum of 32km, otherwise the external temperature will be false

probeSpeed= 6 #In m/s

timeTo11kmAltitude = 11000 / probeSpeed
timeTo20kmAltitude = 20000 / probeSpeed
flightDuration= maxAltitude / probeSpeed

initialTemp=277

temp11Km=217
temp20km=temp11Km
temp32km=229
tempCoefficient20_32km = ((temp32km-temp20km) / (32000-20000))*probeSpeed
tempCoefficient0_11km = ((temp11Km-initialTemp) / (11000-initialAltitude))*probeSpeed

# Constant values needed to find the thermal diffusion
cp= 1400 # Specific Heat in J/kg*K
rho= 35 # Density in kg/m^3
k= 0.027 # Thermal Conductivity in W/m*K
thermalDiffusion= k /(rho*cp) # thermal diffusion in m^2/s
    
intTemp=[] #Array which saves the internal temperature of a simulation
minIntTemp=[] #Array which saves the minimal internal temperature of each simulation
thicknessArray=[] #Array which contains every thickness to try
legendArray=[] #Array which aims to contain the legends for the plot


thicknessArray=arrayThickness(thicknessLimitDown,thicknessLimitUp,thicknessDividers)

for h in range(0,len(thicknessArray)):
    legendArray.append(str(round(thicknessArray[h]*100,2))+' cm')



#Defining the plot
value_height=11
value_width=9
fig=plt.figure(1)
fig.set_figheight(value_height)
fig.set_figwidth(value_width)
plt.subplot(2,1,1)
plt.grid(True)


#For each thickness
for nbSim in range(0,len(thicknessArray)):
    
    thickness=thicknessArray[nbSim] # Getting the thickness in the array
    thicknessStep=thickness/10 # Thickness step
    timeStep=(thicknessStep**2)/(20*thermalDiffusion) # Limite à respecter pour que le programme ne diverge pas

    # Dimension of the time array
    dimTimeArray=int(flightDuration/timeStep)

    # Dimension representing the number of 'slices' of wall
    dimThicknessArray=thickness/thicknessStep
    
    Tn_1=[]
    Tn=[]

    # Array saving the internal temperature of a simulation
    intTemp.append([initialTemp])

    # External temperature for each time step
    extTemp=externalTemp(dimTimeArray,tempCoefficient0_11km,tempCoefficient20_32km,initialTemp,timeTo11kmAltitude,timeTo20kmAltitude,timeStep)

    # Initializing the arrays
    Tn_1,Tn = tempArrayInitialization(dimThicknessArray,initialTemp,Tn_1,Tn)
    intTemp = intTempEquation(Tn_1,Tn,dimTimeArray,dimThicknessArray,thicknessStep,timeStep,extTemp,thermalDiffusion,nbSim,intTemp)

    #Getting the plot for the thickness number nbSim
    t=np.arange(0,dimTimeArray,1)
    plt.plot((timeStep*t/60),intTemp[nbSim])
    
    print('Simulation ',round(thickness*100,2),' cm Done')

plt.legend(legendArray)     
plt.xlim(0,flightDuration/60)
plt.ylim(temp11Km-273.15,(initialTemp-273.15))
plt.xlabel("Flight Duration while ascending (in mn)")
plt.ylabel("Internal Temperature (in celsius)")

'''
plt.subplot(313)
t= np.arange(1,len(extTemp)+1,1)
plot(t,extTemp,"x","y")
plt.show()
'''


minIntTemp= getMinIntTemp(intTemp,thicknessArray)
plt.subplot(2,1,2)
plot(thicknessArray,minIntTemp,"Thickness of the wall (in meter)","minimum temperature reached (in Celsius)")
plt.figtext(0.05,0.65, "Initial Temperature = %.2f C°"%(initialTemp-273.15))
plt.figtext(0.05,0.6, "Inital Altitude = %i m"%initialAltitude)
plt.figtext(0.05,0.55, "Maximum Altitude = %i m"%maxAltitude)
plt.figtext(0.05,0.45, "Average Probe Speed = %.2f m/s"%probeSpeed)
plt.figtext(0.05,0.4, "Minimum Temperature Reached = %.2f C"%minIntTemp[0])
plt.subplots_adjust(left=0.5)
plt.show()
print('Done')
