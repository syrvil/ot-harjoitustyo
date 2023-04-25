# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista selata, lisätä tai muokata kuvilla olevia tunnisteita tai _tageja_. Tunnisteita voidaan käyttää kuvien luokittelmiseen tai opetusmateriaalina koneoppmisessa, jonka avulla on tarkoitus luokietella uusia kuvia tai tunnistaa niissä olevia asioita automaattisesti.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_. 

## Käyttöliittymäluonnos

Käyttöliittymässä on näkymä yhdelle kuvalle ja toiminnallisuuksia, joilla kuvia voi vaihtaa ja käsitellä tunnisteita.

## Perusversion tarjoama toiminnallisuus

### Kuvien lataaminen katseltvaksi ja muokattavaksi
- Käyttäjä voi ladata tiedostoon tai tietokotaan tallennettuja kuvia katseltavaksi tai muokattavaksi - TEHTY
- Käyttäjä voi ladata uusia kuvia käsittelyä varten koneen paikallisesta hakemistosta - TEHTY
- Käyttäjä voi selata kuvia kuvanäkymässä kuva kerrallaan - TEHTY

### Kuvien tunnisteiden muokkaaminen
- Käyttäjä voi lisätä tai poistaa kuvilla olevia tunnisteita - TEHTY

### Kuvien hakeminen tunnisteiden perusteella
- Käyttäjä voi hakea tunnisteiden nimillä kuvia selailtavaksi tai muokattavaski -TEHTY

### Tunnisteiden tilastotietojen katselu
- Käyttäjä voi katsoa statistiikkaa tunnisteiden määristä ja jakaumista

### Kuvien ja tunnisteiden tallentaminen
- Käyttäjä voi tallentaa kuvat, joiden tunnisteita on muokatuu - TEHTY

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Kuvia voi hakea paikasta x internetissä ja tallentaa paikkaan y internetissä
- Mahdollisuus muokata kuvia, esim. muuttaminen mustavalkoiseksi/värilliseksi, koon muuttaminen, rajaus, kiertäminen
- Tekoäly ehdottaa automaattisesti kuville sopivia tunnisteita

## Alustava toteutussuunnitelma
1. versio (VALMIS):
- Kuvien tietorakenne esimerkiksi JSON-tiedostossa, joka sisältää kuvan nimen ja tunnisteet
- Toimintalogiikka, jonka avulla kuvien tietorakennetta voi muokata perustoiminnallisuuksien avulla
- Yksinkertainen tekstikäyttöliittymä toimintoja varten
2. versio (VALMIS): 
- Kuvien lisääminen tietorakenteeseen esimerkiksi polkuna kuvien sijaintiin
- Tekstipohjaisen käyttöliittymän korvaaminen yksinkertaislella graafisella käyttöliittymällä
3. Versio
- Tietojen tallanneus JSON:in sijaan tietokantaan (VALMIS)
- Käyttöliittymän muokkausta ja toiminnallisuuksien lisäämistä
