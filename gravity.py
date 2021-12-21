import pandas as pd
import csv

df=pd.read_csv("final_data")

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]


def convert_to_si_unit(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si_unit(radius,mass)

def gravityCalculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravityCalculation(radius,mass)

df["Gravity"] = gravity
df.to_csv("star_with_gravity.csv")

