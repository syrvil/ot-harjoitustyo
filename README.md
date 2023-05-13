# Image Tagging App

Sovelluksen avulla käyttäjän on mahdollista selata, lisätä tai muokata kuvilla olevia tunnisteita tai tageja. Tunnisteita voidaan käyttää kuvien luokittelmiseen tai opetusmateriaalina koneoppmisessa, jonka avulla on tarkoitus luokietella uusia kuvia tai tunnistaa niissä olevia asioita automaattisesti.

## Python-versiot

Sovelluksen toiminta on testattu Python-versioilla `3.8.16` ja `3.10.6`.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Muutosloki](./dokumentaatio/changelog.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Julkaisut (Release)](https://github.com/syrvil/ot-harjoitustyo/releases/)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

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

## Koodin laatu

Pylint-tarkistuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```
