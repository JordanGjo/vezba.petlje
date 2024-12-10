import time
pocetna_pozicija = 0
cilj = 50

trenutna_pozicija = 0
brzina = 10

for x in range (10):
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("Stigao do cilja.")
    elif trenutna_pozicija > cilj:
        print("presli ste")
        break
    elif trenutna_pozicija < cilj:
        print("niste jos stigli")        
    trenutna_pozicija += brzina
    time.sleep(1)

# ovo je proba za dodavanje druga grana