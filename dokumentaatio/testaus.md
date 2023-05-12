# Testausdokumentti

Ohjelmaa on testattu unittestin automatisoiduilla yksikkö- ja integraatioteistellä sekä järjestelmätasolla manuaalisesti. 

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaava `ImageManager`-luokka tetstaan TestImageManager-testiluokalla. Luokan yksikkötestejä varten alustetaan `ImageManager`-olio sekä testiluokan attribuutteeja, jotka toimivat syötteinä sekä tulosteina testeille.

Integraatiotestejä varten luodaan oma erillinen `ImageManager`-olio, jolle injektoidaan riippuvuuksiksi valekomponentit `ImageRepository` ja `FileRepository` luokista (`DbFileStub`-luokka), jotka simuloivat luokkien metodien toimintaa, mutta tiedot ovat tallennettu keskusmuistiin tietokannan ja tiedostojen sijaan. Tällöin testejä varten ei tarvitse populoida erkiseen dataa tietokantaan tai luoda erillsiä testitiedostoja.

### Repositorio-luokat

`ImageRepository`-luokkaa testataan TestImageRepository-testiluokalla, jolle injektoidaan `ImageRepository`-olio. Tällöin saadaan alustettu uusi tyhjä testitietokanta testejä varten. Testietietokantaan tallennetaan testidataa yksikkötestien yhteydessä, jota sitten käytettään luokan metedion testaamiseen.

Vastaavasti `FileRepository`-luokan olio injektoidaan TestFileRepository-testiluokalle. Testejä varten ei luoda omaan testidataa, vaan testeissä hyödynnetään `image_files\samples` hakemistossa olevia kuvatiedostoja.

### ImageObject-luokka

`ImageObject`-luokkaa testataan TestImageObject-testiluokalla. Luokasta testataan vain sen sisäistä apumetodia, jonka tehtävänä on muuntaa mahdolliset isoja kirjaimia sisältävät tagit pienellä kirjoitetuksi. 

### Testauskattavuus

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


