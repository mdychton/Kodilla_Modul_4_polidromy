import re

# 1️⃣ Usuwanie wszystkich „śmieci” (tylko litery i cyfry zostają)
#    r'[^a-z0-9]' => ^ w nawiasach [] neguje, czyli wszystko poza a-z i 0-9
tekst = "A man, a plan, a canal: Panama!"
tekst_czysty = re.sub(r'[^a-z0-9]', '', tekst.lower())
# wynik: "amanaplanacanalpanama"
# użycie: czyszczenie tekstu, palindromy, preprocessing danych

# 2️⃣ Usuwanie lub normalizacja spacji
#    r'\s+' => jeden lub więcej białych znaków (spacja, tab, nowa linia)
tekst = "ala    ma   kota"
tekst_norm = re.sub(r'\s+', ' ', tekst)
# wynik: "ala ma kota"
# użycie: normalizacja tekstu, czytelne formatowanie, CSV/TSV itp.

# 3️⃣ Wyciąganie liczb z tekstu
#    r'\d+' => jedna lub więcej cyfr
tekst = "mam 2 koty i 15 psów"
liczby = re.findall(r'\d+', tekst)
# wynik: ['2', '15']
# użycie: parsowanie danych, ekstrakcja liczb

# 4️⃣ Alternatywnie, szybkie usuwanie wszystkiego co nie jest literą/cyfrą/_:
#    r'\W+' => \W = wszystko co NIE jest [a-zA-Z0-9_], '+' = jeden lub więcej
tekst = "Hello, World!_2023"
tekst_czysty2 = re.sub(r'\W+', '', tekst)
# wynik: "HelloWorld_2023"
# użycie: czyszczenie identyfikatorów, nazw plików, user input

# 🔹 Funkcje przydatne w re:
# re.sub(pattern, replace_with, tekst) -> zamienia wszystko pasujące do pattern
# re.findall(pattern, tekst) -> zwraca listę wszystkich dopasowań
# re.match(pattern, tekst) -> sprawdza dopasowanie na początku tekstu
# re.search(pattern, tekst) -> szuka dopasowania w całym tekście


tylko litery i cyfry (lepsza wersja)
r'\W+'

👉 usuwa wszystko co NIE jest:

literą
cyfrą
_


re.sub(r'[^a-z0-9]', '', tekst.lower())