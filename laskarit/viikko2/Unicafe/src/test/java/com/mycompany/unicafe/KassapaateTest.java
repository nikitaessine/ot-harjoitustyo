/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author nikitaes
 */
public class KassapaateTest {
    
    Kassapaate kassa;
    Maksukortti kortti;
    
    @Before
    public void setUp() {
        kassa = new Kassapaate();
        kortti = new Maksukortti(1000);
    }
    
    @Test
    public void kassapaateJaLounaatOlemassa(){
        assertTrue(kassa.kassassaRahaa() == 100000);
        assertTrue(kassa.maukkaitaLounaitaMyyty() + kassa.edullisiaLounaitaMyyty() == 0);
    }
    
    @Test
    public void kateisOstoToimii(){
        kassa.syoEdullisesti(240);
        assertEquals(kassa.kassassaRahaa(),100240);
        kassa.syoMaukkaasti(400);
        assertEquals(kassa.kassassaRahaa(), 100640);
        kassa.syoEdullisesti(260);
        assertEquals(kassa.kassassaRahaa(),100880);
        kassa.syoMaukkaasti(420);
        assertEquals(kassa.kassassaRahaa(), 101280);
        
        
    }
    
    @Test
    public void lounaidenMaaraOikein(){
        kassa.syoEdullisesti(240);
        assertEquals(kassa.edullisiaLounaitaMyyty(),1);
        kassa.syoMaukkaasti(400);
        assertEquals(kassa.maukkaitaLounaitaMyyty(),1);
    }
    
    @Test
    public void maksuEiRiittava(){
        kassa.syoEdullisesti(200);
        assertEquals(kassa.kassassaRahaa(),100000);
        kassa.syoMaukkaasti(340);
        assertEquals(kassa.kassassaRahaa(), 100000);
        assertTrue(kassa.edullisiaLounaitaMyyty() == 0);
        assertTrue(kassa.maukkaitaLounaitaMyyty() == 0);
    }
    
    @Test
    public void korttiMaksuToimii(){
        assertTrue(kassa.syoEdullisesti(kortti));
        assertTrue(kassa.syoMaukkaasti(kortti));
    }
    
    @Test
    public void lounaidenMaaraOikeinKortilla(){
        kassa.syoEdullisesti(kortti);
        assertEquals(kassa.edullisiaLounaitaMyyty(),1);
        kassa.syoMaukkaasti(kortti);
        assertEquals(kassa.maukkaitaLounaitaMyyty(),1);
    }
    
    @Test
    public void saldoEiRiittava(){
        kortti.otaRahaa(700);
        assertFalse(kassa.syoMaukkaasti(kortti));
        assertEquals(kortti.saldo(),300);
        assertEquals(kassa.maukkaitaLounaitaMyyty(),0);
        kortti.otaRahaa(200);
        assertFalse(kassa.syoEdullisesti(kortti));
        assertEquals(kortti.saldo(),100);
        assertEquals(kassa.edullisiaLounaitaMyyty(),0);
        
    }
    
    @Test
    public void kortinJaKassanRahamaaraMuuttuu(){
        kassa.lataaRahaaKortille(kortti, 1000);
        assertEquals(kassa.kassassaRahaa(), 101000);
        assertEquals(kortti.saldo(), 2000);
        kassa.lataaRahaaKortille(kortti, -1000);
    }
    
    
        
        
    

    // TODO add test methods here.
    // The methods must be annotated with annotation @Test. For example:
    //
    // @Test
    // public void hello() {}
}
