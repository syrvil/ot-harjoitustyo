## Viikko 3
- Tehty 1. mockup-versio, jossa tekstikäyttöliittymä ja lukee dataa json-tiedostosta ja tallentaa siihen
- Tehty testejä Id, Image ja ImageManager luokille.
## Viikko 4
- Luovuttu mockup-versiosta ja tehty 1. GUI-versio
- Luotu alustava lopullinen arkkitehtuuri, joka eriyttää toimintalogiikan käyttöliittymsätä ja noudattaa repository-mallia
- luotu ja päivitetty konfiguraatiotiedostoja, jotka tukevat uutta arkkitehtuuria
- Lisätty GUI:hin toiminnallisuudet tagien lisäämiseksi, poistamiseksi ja kuvien etsiminen tagien avulla
- Luotu uusi ImageManager luokka ja eriytetty siihen toiminnallisuuksia GUI:sta ja tiedostojenkäsittelyluokasta (FileRepository)
- Nimetty Image luokka ImageObject luokaksi, jotta nimeäminen erottuu Pillow:in (PIL) Image luokasta 
- Muokattu testit toimimaan arkkitehtuurin luokkarakenetene mukaisesti
## Viikko 5
- Lisätty toiminnallisuus, jonka avulla sovellukeen voi lisätä uusia kuvatiedostoja käsiteltäväksi.
- Lisätty tallennustoiminnallisuus (Save) jolla uudet kuvat tai muutokset tageihin voidaan tallentaa.
- Muokattu käyttöliittymän toimintalogiikkaa siten, että uusille kuville, etsityille kuville ja kaikille kuville on oma muuttuja sekä tilamuuttuja, joka seuraa missä tilanäkymässä ollaan.
- Muutettu "Restore Defaults" napin nimi "Show All", jotta uusien kuvien lisäys-, haetut kuvat ja kaikki kuvat näkymät muodostaisivat loogisen kokonaisuuden käytettävyyden ja muutosten tallentamisen näkökulmasta.
- Muutettu hieman painikkeiden sijainteja, jotta käyttökokemus olisi looginen. 
- Sqliten käyttöönotto ja sitä varten uusi luokka DatabaseRepository
- Tietojen tallentaminen oikeasti tietokantaan ohjelman ajoaikaisten muuttujien lisäksi, jos käyttäjä painaa "Save" nappia
- Kovakoodattujen tiedostopolkujen siirtoja muuttujiksi config.py -tiedostoon 
- Koottu staattisia tietokantafunktioita(tietokannan alustus, yhteyden luonti) samaan luokkaan
- ImageManager luokan testin muokkausta tietokannan käyttöönoto seurauskena ja muutamia lisätestejä
