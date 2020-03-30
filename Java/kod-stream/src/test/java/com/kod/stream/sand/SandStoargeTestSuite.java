package com.kod.stream.sand;

import org.junit.Assert;
import org.junit.Test;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class SandStoargeTestSuite {
    @Test
    public void testGetSandBeansQuantity(){
        //Assume
        List<SandStorage>continents = new ArrayList<>();

        continents.add(new Europe());
        continents.add(new Africa());
        continents.add(new Asia());
        //Action
        BigDecimal totalSand = BigDecimal.ZERO;
        for(SandStorage continent : continents){
            totalSand = totalSand.add(continent.getSandBeansQuantity());
        }
        //Assert
        BigDecimal expectedSand = new BigDecimal("211111110903703703670");
        Assert.assertEquals(expectedSand, totalSand);

    }
    @Test
    public  void testGetSandBeansQuantityWithReduce(){
        //Assume
        List<SandStorage>continents = new ArrayList<>();
        continents.add(new Europe());
        continents.add(new Africa());
        continents.add(new Asia());
        //Action
        BigDecimal totalSand = continents.stream()
                .map(SandStorage::getSandBeansQuantity)
                .reduce(BigDecimal.ZERO, (sum, current)->sum.add(current));
        //Assert
        BigDecimal expectedSand = new BigDecimal("211111110903703703670");
        Assert.assertEquals(expectedSand, totalSand);
    }
}
