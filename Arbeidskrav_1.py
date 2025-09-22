# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 - PY1010 
Ann Cathrin Langfeldt
Sist oppdatert 2025.09.22
"""

#Forsikringskostnader
TFA = 3.38 * 365 #Trafikkforsikringavgift for bensin og Elbil- årlig
ElF = 5000 #Forsikring Elbil - årlig
BF = 7500 #Forsikring bensinbil - årlig

#Kjørelengde
KL = 10000 #årlig kjørelengde

#Kostnader drivstoff og bom elbil
ElDF = 0.2 #Drivstofforbruk elbil - KWH per KM
SP = 2 #Strømpris per kwh
ElDK = KL * ElDF * SP #Drivstoffkostnad elbil - årlig
ElBA = KL * 0.1 #Bomavgift elbil

#Kostnader drivstoff og bom bensinbil
BDF = 1 #Drivstofforbruk bensninbil - per km
BDK = KL * BDF #Drivstoffkostnad bensinbil - årlig
BBA = KL * 1.3 #Bomavgift bensninbil


#Totale kostnader elbil vs bensinbil
ElTK = TFA + ElF + ElDK + ElBA #Totale kostnader elbil - årlig
BTK = TFA + BF + BDK + BBA #Totale kostnader bensinbil - årlig
DIFF = BTK-ElTK #differanse i kostnader mellom bensin og elbil

print ("Elbil koster", ElTK, "kr i året")
print ("Bensinbil koster", BTK, "kr i året")
print ("Det er", DIFF,"rimeligere med elbil i året, sammenlignet med bensinbil")
print ("I estimatet er det ikke tatt med kostnader knyttet til lån eller verdittap")
