#wystaw_ocene
'''
Wystawiamy ocene na podstawie
listy ocen.  
'''

oceny = [3.5, 6, 3.0, 3, 4.0, 3]
suma = sum(oceny)               #sumujemy oceny z listy ocen
liczba_ocen = len(oceny)        #wyznaczamy ilosc elementow listy
srednia = suma / liczba_ocen    #wyliczamy srednia

if  srednia >= 5.5:             #jesli srednia >= 5.5 to dajemy celujacy
    ocena = "celujacy"
elif srednia >= 4.5:            #jesli srednia >= 4.5 to dajemy bardzo dobry
    ocena = "bardzo dobry"
elif srednia >= 3.5:            #jesli srednia >= 3.5 to dajemy dobry
    ocena = "dobry"
elif srednia >= 2.5:            #jesli srednia >= 2.5 to dajemy dostateczny
    ocena = "dostateczny"
else:
    ocena = "raczej slabsza"    #w przeciwnym wypadku dajemy ocene slabsza
    
print ('Srednia = ' + str(srednia) )

print ('Ocena: ' + ocena)
