# Image Tagging App

Sovelluksen avulla käyttäjän on mahdollista selata, lisätä tai muokata kuvilla olevia tunnisteita tai tageja. Tunnisteita voidaan käyttää kuvien luokittelmiseen tai opetusmateriaalina koneoppmisessa, jonka avulla on tarkoitus luokietella uusia kuvia tai tunnistaa niissä olevia asioita automaattisesti.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Muutosloki](./dokumentaatio/changelog.md)
- [Viikon 5 julkaisu (Release)](https://github.com/syrvil/ot-harjoitustyo/releases/tag/viikko5)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

⚠️ **Huom! Ajettaessa Pytest-testejä laitoksen Cubbli Linux -virtuaalityöasemassa www-selaimen kautta tuli vastaavanlainen tietokantavirheilmoitus kuin tässä [ohjeessa](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla), vaikka minkäänlaista tietokantaa ei edes ollut käytössä. Ohjeessa esitetty ratkaisu toimi myös tässä tapauksessa.**

⚠️ **Huom2! VMWare Horizon Clientillä edellä mainittua ongelmaan ei tullut testien ajamisen yhteydessä.**

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
