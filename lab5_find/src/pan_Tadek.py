ksiazka = open("pan-tadeusz.txt", mode="r", encoding="utf-8")
tekst = ""
slowa = []
for linia in ksiazka:
    tekst += linia
    nowe_slowa = [slowo for slowo in linia.strip().split() if slowo != ""]
    slowa += nowe_slowa
