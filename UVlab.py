#UV Spectra in Solution
#@Shane Gervais
#3620569
#This code is made to plot and
#analyze our UV data from our
#lab in CHEM4616 with Dr. Kassimi.

#Import methods that will help us for the analysis
import pandas as pd
import io
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np



#Integrates the excel sheet containing our data
water = pd.read_excel('Water.xlsx')
ethanol = pd.read_excel('Ethanol.xlsx')
hexane = pd.read_excel('Hexane.xlsx')

#Defining our variables
absorptionW = water.Abs
wavelengthW = water.Wavelength
absorptionW = np.array(absorptionW)
wavelengthW = np.array(wavelengthW)

absorptionE = ethanol.Abs
wavelengthE = ethanol.Wavelength
absorptionE = np.array(absorptionE)
wavelengthE = np.array(wavelengthE)

absorptionH = hexane.Abs
wavelengthH = hexane.Wavelength
absorptionH = np.array(absorptionH)
wavelengthH = np.array(wavelengthH)


#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelengthE,absorptionE,'r-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()

#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelengthH,absorptionH,'g-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()

#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelengthW,absorptionW,'b-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()


#Finds our peaks for each wave segments
#and appends them in an array called peaks
#Water
peakW = []
for i in range(0, len(absorptionW)):
    if absorptionW[i] == max(absorptionW):
        peakW.append(i)


peakWaveW = wavelengthW[peakW[0]]
print("The peak Wavelength for acetone in water is at ", peakWaveW, " nm")



#Ethanol
peakE = []
for i in range(0, len(absorptionE)):
    if absorptionE[i] == max(absorptionE):
        peakE.append(i)


peakWaveE = wavelengthE[peakE[0]]
print("The peak Wavelength for acetone in ethanol is at ", peakWaveE, " nm")



#Hexane
peakH = []
for i in range(0, len(absorptionH)):
    if absorptionH[i] == max(absorptionH):
        peakH.append(i)


peakWaveH = wavelengthH[peakH[0]]
print("The peak Wavelength for acetone in hexane is at ", peakWaveH, " nm")



#Finding Energy
h = 6.626*pow(10, -34)
c = 3*pow(10, 8)
fW = c/(peakWaveW*pow(10, -9))
fE = c/(peakWaveE*pow(10, -9))
fH = c/(peakWaveH*pow(10, -9))

energyW = h*fW
energyE = h*fE
energyH = h*fH

print("The excitation energy of acetone in ethanol is ", energyE,"J for hexane is ", energyH, "J and for water ", energyW, "J")


#Hydrogen bonding energy
#Since H bonding in hexane is neglible
#if we subtract our hexane's energy with the 
#other solvents we get the HBE of each solvent
hbeW = energyW - energyH
hbeE = energyE - energyH
print("The Hydrogen bonding energy of water is: ", hbeW, "J and for ethanol", hbeE, "J")


#Molar extinction coefficient
l = 1 #cm
p = 784 #g/L
vAcetone = 0.12/1000 #L
m = p*vAcetone #g
molarmass = 58.08 #g/mol
n = m/molarmass #mol
vSolution = 0.01 #L
con =n/vSolution#mol/L
print("The concentration of acetone in solution is: ", con, " mol/L")

eE = energyE/n
eW = energyW/n
eH = energyH/n

print("The energy per mol of acetone in water is ", eW, "J/mol")
print("The energy per mol of acetone in ethanol is ", eE, "J/mol")
print("The energy per mol of acetone in hexane is ", eH, "J/mol")

hbondEnergyW = eW - eH
hbondEnergyE = eE - eH
print("The Hydrogen bonding energy of water is: ", hbondEnergyW, " J/mol and for ethanol", hbondEnergyE, "J/mol")


#Water
epsiW = (max(absorptionW))/(con*l)
print("The molar extinction coefficient for water solution is: ", epsiW, " L/mol*cm")

#Ethanol
epsiE = (max(absorptionE))/(con*l)
print("The molar extinction coefficient for ethanol solution is: ", epsiE, " L/mol*cm")

#Hexane
epsiH = (max(absorptionH))/(con*l)
print("The molar extinction coefficient for hexane solution is: ", epsiH, " L/mol*cm")





