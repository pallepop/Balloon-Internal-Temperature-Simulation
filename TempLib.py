import matplotlib.pyplot as plt

def arrayThickness(thicknessLimitDown,thicknessLimitUp,thicknessDividers):
    
    arrayThickness=[]
    
    for i in range(int(thicknessLimitDown/thicknessDividers),int(round((thicknessLimitUp+thicknessDividers)/thicknessDividers))): #Defining what thickness are going to be simulated
        arrayThickness.append(i*thicknessDividers)
        
    return arrayThickness


def externalTemp(dimTimeArray,tempCoefficient0_11km,tempCoefficient20_32km,initialTemp,timeTo11kmAltitude,timeTo20kmAltitude,timeStep): #computing the external temprature from 0 to 32 km
    
    extTemp=[initialTemp]
    
    for i in range(1,dimTimeArray):
        if (i <= (timeTo11kmAltitude-1)/timeStep):
            extTemp.append(extTemp[i-1]+(tempCoefficient0_11km*timeStep))
            
        elif (i > (timeTo11kmAltitude-1)/timeStep and i <= (timeTo20kmAltitude-1)/timeStep ): 
            extTemp.append(extTemp[round((timeTo11kmAltitude-1)/timeStep)-1])

        elif (i > (timeTo20kmAltitude-1)/timeStep):
            extTemp.append(extTemp[i-1]+(tempCoefficient20_32km*timeStep))
        
    return extTemp

def tempArrayInitialization(dimThicknessArray,initialTemp,Tn_1,Tn): #Setting the initial temperature everywhere in the insulation
    
    for v in range(0,int(dimThicknessArray)+1):
        Tn_1.append(initialTemp)
        Tn.append(0)
        
    return Tn_1,Tn

def intTempEquation(Tn_1,Tn,dimTimeArray,dimThicknessArray,thicknessStep,timeStep,extTemp,thermalDiffusion,nbSim,intTemp):
    
    for c in range(1, dimTimeArray):
        Tn[0]=extTemp[c]#We define the first value at the edge of the insulation (outside) by the external temperature
        for j in range(1,int(dimThicknessArray)):
            Tn[j]=Tn_1[j]+thermalDiffusion*(timeStep/thicknessStep**2)*(Tn_1[j+1]-2*Tn_1[j]+Tn_1[j-1]) # Simplified heat equation (1-D)
        Tn[-1]=Tn[-2]#Assumption saying the internal temperature of the basket is the same as the one at the edge of the insulation (inside)
        intTemp[nbSim].append(Tn[-2]-273.15)
        Tn_1=Tn
        
    return intTemp
        
def getMinIntTemp(intTemp,thicknessArray): #Getting the minimum internal temperature of each simulation
    
    minIntTemp=[]
    
    for i in range(0,len(thicknessArray)):
        minIntTemp.append(min(intTemp[i]))
    return minIntTemp

def plot(x,y,xAxisName,yAxisName):
    
    plt.plot(x,y)
    plt.xlabel(xAxisName)
    plt.ylabel(yAxisName)
    plt.grid(True)
