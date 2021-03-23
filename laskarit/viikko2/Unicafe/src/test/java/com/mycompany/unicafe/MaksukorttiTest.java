package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void kortinSaldoAlussaOikein(){
        assertEquals("saldo: 10", kortti.toString());
    }
    
    @Test
    public void saldonKasvatusOikein(){
        kortti.lataaRahaa(20);
        assertEquals("saldo: 30", kortti.toString());
        
    }
    
    @Test
    public void saldoVaheneeOkein(){
        kortti.otaRahaa(2);
        kortti.otaRahaa(4);
        assertEquals("saldo: 4", kortti.toString());
    }
    
    @Test
    public void saldoEiMuutu(){
        kortti.otaRahaa(4);
        kortti.otaRahaa(8);
        assertEquals("saldo: 6", kortti.toString());
    }
    
    @Test
    public void rahatRiittavat(){
        kortti.otaRahaa(8);
        kortti.otaRahaa(12);
        assertTrue(kortti.saldo() >= 0);
        assertFalse(kortti.saldo() < 0);
    }
}
