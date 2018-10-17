Authors:
    - aar, Andreas Arnesson
    - efo, Emil Folino
Revisions:
    - "2018-06-28": (A, efo) individuella examinationen 2018-lp1.


Individuell examination (prep)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.

För alla uppgifter du löser, uppdatera funktionens docstring (kommentaren längst upp i funktionen) till en relevant kommentar om vad funktionen gör.

När du vill under hela examinationen kan du köra kommandot `dbwebb exam correct prep` för att rätta dina lösningar och se hur många poäng du har uppnått.

Utöver att lösa uppgifterna behöver du se till att alla filer validera med `dbwebb validate prep`.

Du har 5 timmar på dig att lösa uppgifterna och publicera dina lösningar med kommandot `dbwebb exam seal prep` inom tidsramen. Den sista `seal` som görs inom tidsramen är den som kommer användas som betygsunderlag.

**För att få godkänt på examinationen måste du klara uppgift 1.**

Följande tabell används vid bedömning av den individuella examinationen.

| Bedömningspunkt | Poäng | Din poäng |
|-----------------|-------|-----------|
| Uppgift 1 är implementerad och fungerar enligt specifikationen. | 20 | |
| Uppgift 2 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 3 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 4 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 5 är implementerad och fungerar enligt specifikationen. | 10 | |
| TOTALT | 60 | |

Tillsammans med kursmoment 01-06 ger dessa poäng ditt slutbetyg, [Bedömning och betygsättning](http://dbwebb.se/kurser/faq/bedomning-och-betygsattning-individuell).


Uppgifter
---------------------------------

1. **Analysera text**. Den här uppgiften går ut på att du ska analysera textfilen "myths.txt" på 2 olika sätt. `analyze_text` funktionen ska innehålla en while-loop som tar emot input från användaren. Loopen ska avslutas om användaren skriver "q" eller "quit", när programmet avslutas ska funktionen returnera sant, `True`.
De två olika sätten texten ska analyseras på är:
    - Om användaren skriver "s" som input ska antalet meningar som finns i varje paragraph beräknas. Skriv ut antalet meningar som finns i de tre paragrafer som har flest meningar. Skriv ut med `print()`. Skriv enbart ut siffran sorterad från högst till lägst, ingen extra text.
    - Om användaren skriver "g" som input ska du räkna hur många gånger gudarnas namn nämns i varje paragraf. För topp tre paragrafer skriv ut antalet gånger gudarna nämns, skrivas ut med `print()`. Skriv enbart ut siffran, sorterad från högst tilllägst, ingen extra text. följande gudar finns i texten, "Odin,Thor,Hödur,Baldur,Tyr,Heimdall,Vidar,Vali,Loki,Frigga,Freya,Nanna,Iduna,Sif,Modi,Magni".

 Funktionen analyze_text ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval, utom valet "q". Om användaren skriver ett ej giltigt argument ska "Not an option!" skrivas ut. Gör inga extra `print()` i din lösning förutom de som efterfrågas i kravspecifikationen. En paragraf separeras med två "\n".

2. **Kontrollera HEX-koder**. Fyll i funktionen `verify_hex`, den ska ta emot ett argument, en sträng. Funktionen ska sedan kontrollera om strängen är en giltig hex-kod för en färg. Funktionen ska returnera sant, True, om hex-koden är giltig, annars falskt, False.

 För att en sträng kan godkännas gäller följande krav:
    - Strängen börjar med en brädgård '#'.
    - Strängen består sedan av 3 eller 6 hexadecimala siffror 0-f.
    - Alla bokstäver ska vara små bokstäver.<br><br>
