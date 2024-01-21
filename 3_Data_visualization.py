#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:23:19 2023

@author: School
"""

import pandas as pd

# Lees de dataset in
data = pd.read_csv('deliverytime.csv')

import matplotlib.pyplot as plt

df = pd.DataFrame(data)

df_filtered = df[(df['Delivery_person_Ratings'] <= 5) & (df['Delivery_person_Age'] >= 16)]

# Tellen hoe vaak iedere voertuig voorkomt
naam_frequentie = df_filtered['Type_of_vehicle'].value_counts()

# Maak een pie chart van de frequentie van voertuigen
plt.figure(figsize=(6, 6))
plt.pie(naam_frequentie, labels=naam_frequentie.index, autopct='%1.1f%%', startangle=140)
plt.title('Frequentie van bezorg voertuig')
plt.axis('equal')  # Zorgt ervoor dat de cirkel eruitziet als een cirkel

# Laat de pie chart zien
plt.show()

# Maak een scatter plot voor leeftijd vs rating
plt.figure(figsize=(9, 6))
plt.scatter(df_filtered['Delivery_person_Ratings'], df_filtered['Delivery_person_Age'], c='b', marker='o', edgecolors='k', alpha=0.7)
plt.ylabel('Leeftijd van Bezorger')
plt.xlabel('Rating van Bezorger')
plt.title('Leeftijd versus Rating voor Bezorgers')
plt.grid(True)

#  Laat de grafiek zien
plt.show()