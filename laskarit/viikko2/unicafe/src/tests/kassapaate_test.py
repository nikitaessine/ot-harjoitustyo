import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        
    
    def test_kassapaatteen_saldo(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edulliset_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaat_myyty(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisella_osto_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_kateisella_rahaeiriita_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    
    def test_kateisella_osto_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_kateisella_rahaeiriita_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kortilla_eirahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla_eirahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000), None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)
    
    def test_lataa_rahaa_kortille_nega(self):
        self.maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100), None)
