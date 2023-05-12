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

### Asennus ja konfigurointi

### Toiminnallisuudet

## Sovellukseen jääneet laatuongelmat


