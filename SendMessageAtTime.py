# Door: Almer de Vries  |   almerdvries@gmail.com
# Datum: 25052020
# SendMessageAtTime.py
# Versie: 1

# Importeer bibliotheken
import keyboard     # Zorgt ervoor dat ik het toetsenbord kan gebruiken met Python
import time         # Hiermee kan ik een vertraging maken
import datetime     # Alles met betrekking tot datum en tijd
import sys          # Maakt het mogelijk het programma uit zichzelf af te sluiten

while True:                                         # while | Maakt een oneindige loop
   # Ververst de tijd
   currentDT = datetime.datetime.now()              # datetime | Geen idee wat het doet. Volgens mij ververst het de tijd.

   # Instellingen en waarden
   tijd_huidig = currentDT.strftime("%H%M")         # String | Slaat de huidige tijd (uur en minuut) op in een string als 1 getal. Bijvoorbeeld 2231 (22:31)
   tijd_trigger = "2240"                            # String | De tijd waarop je wilt dat het bericht wordt gestuurd
   bericht = "First (Made with Python)\n"           # String | Bericht dat later wordt verstuurd
   delay = 0.1                                      # int | Vertraging tussen elke loop van dit programma in seconden

   # Loop
   if(tijd_huidig == tijd_trigger):                 # if | Wanneer de huidge tijd gelijk is aan de trigger tijd (wanneer beide strings hetzelfde zijn) dan uitvoeren
       keyboard.write(bericht),                     # keyboard | Typt het vooraf ingestelde bericht
       print("Triggered"),                          # Python | Typt een bevestigingsbericht in de console (zwarte scherm)
       sys.exit(0)                                  # sys | Sluit het programma af

   # Overig
   print(tijd_huidig)                               # Python | Typt de huidige tijd in de console (zwarte scherm)
   time.sleep(delay)                                # time | Kleine vertraging voordat het programma opnieuw naar de tijd kijkt
  
# Gebruikte links:
#   - https://tecadmin.net/get-current-date-time-python/
#   - https://stackoverflow.com/questions/2823472/is-there-a-method-that-tells-my-program-to-quit
#   - https://pypi.org/project/keyboard/
# Als je maar genoeg Googled kan je alles maken ;)
