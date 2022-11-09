import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_rahan_lataaminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_raha_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(5)
        self.maksukortti.ota_rahaa(3)
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 2)
    
    def test_saldo_false(self):
        self.maksukortti.ota_rahaa(5)
        self.maksukortti.ota_rahaa(3)
        self.maksukortti.ota_rahaa(5)
        self.assertNotEqual(self.maksukortti.ota_rahaa, True)

    def test_saldo_true(self):
        self.maksukortti.ota_rahaa(5)
        self.maksukortti.ota_rahaa(3)
        self.assertNotEqual(self.maksukortti.ota_rahaa, False)

    def test_saldo_euroina(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.10 euroa" )
