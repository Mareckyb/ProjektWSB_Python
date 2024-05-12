Program zaliczeniowy na studia podyplomowe Python Developer na WSB Merito Gdansk stworzony we frameworku DJANGO (v.5)

Jest to pierwsza wersja aplikacji i w planach sa nastepne wersje rozszerzajace funkcjonalnosc (np. Dasboard i zaawansowane blokady dla uzytkownikow).

Interface programu zostal zbudowany z pomoca frameworka BOOTSTRAP v. 4.5 - biblioteki dolaczone do programu.

Sluzy do logowania zdarzen z roznych zasobow (sekcja ZASOBY) przez RESTAPI i wyswietlania ich w tabeli ZDARZENIA.
RESTAPI obsluguje ENDPOINT /api_zdarzenie/. Za jego pomoca mozna wywolac fukcje GET i POST. RestAPI wymienia dane w formacie JSON.

Administracja uzytkownikami z poziomu endpointu /ADMIN/

Wymagania:
Python 3 (pisane i testowane na 3.10)
Baza danych PostgreSQL (Program testowany na wersji 9)
Zainstalowane biblioteki Pythona z pliku requirements.txt (pip install -r requirements.txt)