personer = []

while True:
    navn = input("Indtast navn: ")
    efternavn = input("Indtast efternavn: ")
    by = input("Indtast by: ")
    postnummer = input("Indtast postnummer: ")
    skole = input("Indtast skole: ")
    klasse = input("Indtast klasse: ")
    alder = int(input("Indtast alder: "))
    
    person = {"navn": navn, "efternavn": efternavn, "by": by, "postnummer": postnummer, "skole": skole, "klasse": klasse, "alder": alder}
    personer.append(person)
    
    svar = input("Vil du tilføje en ny person? (Ja/Nej) ")
    if svar.lower() == "nej":
        break

søgt_alder = int(input("Hvilken alder vil du søge efter? "))
for person in personer:
    if person["alder"] == søgt_alder:
        print(f"{person['navn']} {person['efternavn']} ({person['alder']} år) bor i {person['by']} og går i {person['klasse']} på {person['skole']}.")
