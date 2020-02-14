import unicodedata
import sys
import time
import datetime
import calendar


from os import listdir
from openpyxl import load_workbook

#Value Limits

#Temperature (Celsius)
temp_max = 45
temp_min = -5

#Altimeter Pressao (Barometro) (mm)
pressure_max = 800
pressure_min = 700

#Atmospheric Vapor Tension (mm)
vapor_max = 35
vapor_min = 1

#Humidity (%)
humidity_max = 100
humidity_min = 0

#Ozonometer (in grains)
ozone_max = 20
ozone_min = 0

#Cloud Quantity (int)
cloud_max = 25
cloud_min = 0

#Pluvimeter (mm)
pluv_max = 100
pluv_min = 0

#Udometer (mm)
udo_max = 50
udo_min = 0

#Absolute wind velocity (km)
abso_wind_speed_max = 150
abso_wind_speed_min = 0

#"Velocidade Horaria"
clock_wind_speed_max = 40
clock_wind_speed_min = 0

#Tensao Vapor (mmHg)
HgVapor_max = 20
HgVapor_min = -1

#Insolacao Heliografo de Campbell
insolation_max = 1
insolation_min = 0

#Insolacao Relativa percentagem
insolationPercentage_max = 100
insolationPercentage_min = 0

#Insolacao maxima possivel (total)
totalInsolation_max = 18
totalInsolation_min = 0

#Pressao (mmHg)
HgPressure_max = 70
HgPressure_min = 10


