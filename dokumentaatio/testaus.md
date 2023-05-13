# Testausdokumentti

Ohjelmaa on testattu unittestin automatisoiduilla yksikkö- ja integraatioteistellä sekä järjestelmätasolla manuaalisesti. 

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaava `ImageManager`-luokka tetstaan [TestImageManager](../src/tests/test_image_manager.py)-testiluokalla. Luokan yksikkötestejä varten alustetaan `ImageManager`-olio sekä testiluokan attribuutteeja, jotka toimivat testisyötteinä sekä -tulosteina testeille.

Integraatiotestejä varten luodaan oma erillinen `ImageManager`-olio, jolle injektoidaan riippuvuuksiksi valekomponentit `ImageRepository` ja `FileRepository` luokista (`DbFileStub`-luokka), jotka simuloivat luokkien metodien toimintaa, mutta tiedot ovat tallennettu keskusmuistiin tietokannan ja tiedostojen sijaan. Tällöin testejä varten ei tarvitse populoida erkiseen dataa tietokantaan tai luoda erillsiä testitiedostoja.

### Repositorio-luokat

`ImageRepository`-luokkaa testataan [TestImageRepository](../src/tests/test_image_repository.py)-testiluokalla, jolle injektoidaan `ImageRepository`-olio. Tällöin saadaan alustettu uusi tyhjä testitietokanta testejä varten. Testietietokantaan tallennetaan testidataa yksikkötestien yhteydessä, jota sitten käytettään luokan metedion testaamiseen.

Vastaavasti `FileRepository`-luokan olio injektoidaan [TestFileRepository](../src/tests/test_file_repository.py)-testiluokalle. Testejä varten ei luoda omaan testidataa, vaan testeissä hyödynnetään `image_files\samples` hakemistossa olevia kuvatiedostoja.

### ImageObject-luokka

`ImageObject`-luokkaa testataan [TestImageObject](../src/tests/test_image_object.py)-testiluokalla. Luokasta testataan vain sen sisäistä apumetodia, jonka tehtävänä on muuntaa mahdolliset isoja kirjaimia sisältävät tagit pienellä kirjoitetuksi. 

### Testauskattavuus

### Testaamatta jääneet metodit

Automaattisisen yksikkö- ja integraatiotestaamisen ulkopuolelle on jätetty pääsääntöisesti metodit ja funktiota, jotka lukevat tai kirjoittavat dataa konfiguraatiotiedostoihin. Näitä ovat esimerkiksi:
- `ImageRepository`-luokan metodi `init_db_from_json()`
- `FileRepositry`-luokan metodit `read_conf_file()`, `write_conf_file()` ja `save_image()`
- `initialize_database.py` tiedostossa määritellyt tietokantafunktiot.

Edellä mainitut metodien ja funktioiden toiminta on kuitenkin joutunut epäsuoran testauksen kohteeksi aikaisempien automaattitestien sekä alla mainittujen manuaalisten järjestelmätestien yhteydessä.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovelluken asennusta on testattu hakemalla viimeisin julkaisu GitHubista ja asentamalla se käyttöohjeiden mukaisesti paikallisesti Ubuntu 22.04.2 LTS ympäristöön sekä Cubbli Linux virtuaalityöasemaan VMWare Horizon etätyöpöytäsovelluksen kautta. 

Konfigurointia on testattu muutammalla *.env* tiedoston ympäristömuuttujien arvoja, joissa määritellään hakemistopolkuja ja tiedostonimiä-

### Toiminnallisuudet

Käyttöliittymän ja sen toiminnallisuudet ovat testattu kokeilemalla seuraavia käyttöskneerioita: 

- kaikki painikkeet toimivat kun niitä painetaan 
- kuvat vaihtuvat oikein 
- kuvalistaukset muodustuvat oikein siirryttäessä näkymien välillä 
- suurilla kirjaimilla kirjoitetut tagit muuttuvat pieniksi
- tyhjiä kenttiä ei hyväksytä syötteiksi
- kuvan ja kuvien lataaminen paikallisesta hakemistosta toimii oikein
- paikallisesti ladattu kuva tallentuun oikeaan paikkaan, kun painetaan "Save" nappia
- paikallisesti ladattua kuvaa ei tallenneta, jos siirrytään näkymästä toiseen eikä paineta "Save" nappia

## Sovellukseen jääneet laatuongelmat

Sovelluksen totetutuksessa ja testauksessa on seuraavia puutteita:

- Testitietokannalle ja testiedostoille ei ole määrilety omia konfiguraatiomuuttujia, jolloin paikoitellen käytetään samoja tiedostonimiä ja hakemistopolkuja kuin tuotannossa. Samoin osalle testeistä ei ole muodostettu omaa testidataa, vaan hyödynnetään tuotantodataa. Tämä on hieman sekavaa, vaikkakin testi- ja tyuontaympäristöt ovat eriytetty toisistaan.
- Tiedostojen luku- ja kirjoitusoikeuksia ja tiedostojen puuttumista tai olemassa oloa ei tarkisteta, eikä mahdollisiin virhetilanteisiin reagoida.
- Pääosa syötteiden tarkistuksia ja metodien saamista parametrien arvoista tarkistetaan `ImageApp` ja `ImageManager` luokissa. Jos jostain syystä syötteet ja paramterit saavat virheellisiä arvoja, niiden käsitelyyn ei olla varauduttu muissa luokissa. 
- Edellisestä johtuen testit eivät siis testaa erityisen kaatavasti metodien toimintaa esimerkiksi virheellisten paramtrien kohdalla.
- *Pylint* ilmoittaa liian suuresta määrästä julkisia metodeja (eli siis testeistä) `TestImageManager`-luokan kohdalla. 
