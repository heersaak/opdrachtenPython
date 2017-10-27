bruin = {'Boxtel','Best','Beukenlaan','Eindhoven','''Helmond't Hout''','Helmond','Helmod Brouwhuis','Deurne'}
groen = {'Boxtel','Best','Beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

print('waar groen en bruin beide langskomen:',(groen & bruin))
print('Waar groen en bruin verschillen: ', (groen ^ bruin))
print('Waar bruin en groen verschillen: ', (bruin - groen))
print('groen:', groen)
print('bruin:', bruin)
