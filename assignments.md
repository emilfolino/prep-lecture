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
    - Om användaren skriver "g" som input ska du räkna hur många gånger gudarnas namn nämns i varje paragraf. För topp tre paragrafer skriv ut antalet gånger gudarna nämns, skrivas ut med `print()`. Skriv enbart ut siffran, sorterad från högst tilllägst, ingen extra text.

 Funktionen analyze_text ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval, utom valet "q". Om användaren skriver ett ej giltigt argument ska "Not an option!" skrivas ut. Gör inga extra `print()` i din lösning förutom de som efterfrågas i kravspecifikationen. En paragraf separeras med två "\n".

2. **Kontrollera HEX-koder**. Fyll i funktionen `verify_hex`, den ska ta emot ett argument, en sträng. Funktionen ska sedan kontrollera om strängen är en giltig hex-kod för en färg. Funktionen ska returnera sant, True, om hex-koden är giltig, annars falskt, False.

 För att en sträng kan godkännas gäller följande krav:
    - Strängen börjar med en brädgård '#'.
    - Strängen består sedan av 3 eller 6 hexadecimala siffror 0-f.
    - Alla bokstäver ska vara små bokstäver.<br><br>

3. **Hitta dubbletter**. Fyll i funktionen `find_duplicates`, den ska ta en lista som argument och listan innehåller strängar. Hitta alla dubbletter och returnera en lista med värden som är dubbletter. I den returnerade listan ska varje dubblett endast vara med en gång. Din lösning ska vara case-insensitive, dvs. `a == A`. Listan som returneras ska vara sorterad i bokstavsordning.

4. **Kolla datatyper**. Fyll i funktionen `types`, den ska ta emot en lista som argument. Den listan kan innehålla ett godtyckligt antal element av tre olika datatyper. De möjliga datatyperna är heltal, strängar och listor. Funktionen ska returnera en sträng som byggs upp av beroende på de olika elementen som finns i argumentet. Beroende på datatypen gör följande:
    - Heltal, lägg till strängen "The square of i is x.", där "i" är heltalet och "x" är `i^2`.
    - Sträng, lägg till strängen "The secret word is s.", där "s" är strängen.
    - Lista, lägg till strängen "The list contains x, y, z.", där "xyz" är värden från listan. Listan kan innehålla en odefinierad mängd värden. Du kan anta att elementen är av datatypen sträng.
    - Annan typ, om värdet är av annan typ än de ovanför, gör inget.

 Den returnerade strängen ska innehålla mellanrum mellan de olika strängar som har byggts ihop. Om argumentet är en tom lista ska funktionen returnera en tom sträng. Exempel på argument och resultat är följande, `[2, "hej", ["tre", "fyra", "fem"]]` --> "The square of 2 is 4. The secret word is hej. The list contains tre, fyra, fem.".

5. **Validera email adresser**. Fyll i funktionen `validate_email`, den ska validera en email adress. Funktionen ska returnera sant, True, om adressen är giltig, annars falskt, False.

 Följande regler gäller:
    - innehåller ett "@".
    - det ska finnas karaktärer framför "@".
    - efter @, ska det finnas minst en punkt, ".", och andra karaktärer framför punkten.
    - efter den sista punkten ska det finnas 2 eller 3 karaktärer.
    - innehåller endast karaktärerna a-z och 0-9 samt ".", "_", "-", "@".
    - endast små bokstäver.
