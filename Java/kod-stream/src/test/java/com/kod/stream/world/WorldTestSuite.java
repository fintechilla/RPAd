package com.kod.stream.world;

import org.junit.Test;

import java.math.BigDecimal;

public class WorldTestSuite {
    @Test
    public void testGetPeopleQuantity(){
        //Assume
        Country ce1 = new Country(new BigDecimal("2000111"));
        Country ce2 = new Country(new BigDecimal("2000112"));
        Country ce3 = new Country(new BigDecimal("2000113"));

        Country ae1 = new Country(new BigDecimal("2000111"));
        Country ae2 = new Country(new BigDecimal("2000112"));
        Country ae3 = new Country(new BigDecimal("2000113"));

        World world = new World();

    }
}
