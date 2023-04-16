# Ohjelmistotekniikka 2023, harjoitustyö

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Muutosloki](./dokumentaatio/changelog.md)

⚠️ **Huom! Ajettaessa Pytest-testejä laitoksen Cubbli Linux -virtuaalityöasemassa tuli vastaavanlainen tietokantavirheilmoitus kuin tässä [ohjeessa](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla), vaikka minkäänlaista tietokantaa ei edes ollut käytössä. Ohjeessa esitetty ratkaisu toimi myös tässä tapauksessa.**

## Asennus
1. Asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```
## Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
