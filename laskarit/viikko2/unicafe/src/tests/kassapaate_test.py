import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    ### Kassapaatteen rahat ja lounaiden määrä alussa oikein
    def test_kassapaatteen_rahat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myydyt_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_myydyt_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    ### Käteisostot toimivat oikein edullisten lounaiden osalta
    def test_kateisosto_edullisesti_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateisosto_edullisesti_maksu_riittava_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, (500-240))

    def test_kateisosto_edullisesti_maksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullisesti_maksu_ei_riittava_rahamaara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullisesti_maksu_ei_riittava_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_edullisesti_maksu_ei_riittava_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    ### Käteisostot toimivat oikein maukkaiden lounaiden osalta
    def test_kateisosto_maukkaasti_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateisosto_maukkaasti_maksu_riittava_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, (500-400))

    def test_kateisosto_maukkaasti_maksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukkaasti_maksu_ei_riittava_rahamaara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukkaasti_maksu_ei_riittava_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_maukkaasti_maksu_ei_riittava_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    ### Korttiostot toimivat oikein edullisten lounaiden osalta

    def test_korrtiosto_edullisesti_kortilla_riittavasti_rahaa_palauttaa_True(self):
        self.assertAlmostEqual(
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_edullisesti_kortilla_riittavasti_rahaa_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_edullisesti_kortilla_ei_riittavasti_rahaa_palauttaa_False(self):
        maksukortti = Maksukortti(100)
        self.assertAlmostEqual(
            self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        
    def test_korttiosto_edullisesti_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    ### Korttiostot toimivat oikein maukkaiden lounaiden osalta

    def test_korrtiosto_maukkaasti_kortilla_riittavasti_rahaa_palauttaa_True(self):
        self.assertAlmostEqual(
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_korttiosto_maukkaasti_kortilla_riittavasti_rahaa_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_maukkaasti_kortilla_ei_riittavasti_rahaa_palauttaa_False(self):
        maksukortti = Maksukortti(100)
        self.assertAlmostEqual(
            self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        
    def test_korttiosto_edullisesti_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

### Kortin lataaminen toimii oikein

    def test_kortin_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        
### Kortin lataaminen kasvattaa kassan rahamäärää

    def test_kortin_lataaminen_kasvattaa_kassan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortin_lataaminen_ei_kasvata_kassan_rahaa_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    