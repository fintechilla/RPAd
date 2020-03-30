package com.kod.testing.collection;
import com.kod.testing.collection.OddNumbersExterminator;
import org.junit.*;
import com.kod.testing.collection.OddNumbersExterminator;

import java.util.ArrayList;

public class CollectionTestSuite {
    @Before
    public void before(){
        System.out.println("Test Case: begin");
    }
    @After
    public void after(){
        System.out.println("Test Case: end");
    }
    @BeforeClass
    public static void beforeClass() {
        System.out.println("Test Suite: begin");
    }
    @AfterClass
    public static void afterClass() {
        System.out.println("Test Suite: end");
    }

    @Test
    public void testOddNumbersExterminatorEmptyList(){
        //Given
        OddNumbersExterminator exterminator = new OddNumbersExterminator();
        ArrayList<Integer>emptyList = null;
        //When
        ArrayList<Integer>result = exterminator.exterminate(emptyList);
        //Then
        Assert.assertEquals(null, result);
    }
    @Test
    public void testOddNumbersExterminatorNormalList(){
        //Given
        OddNumbersExterminator exterminator = new OddNumbersExterminator();
        ArrayList<Integer>normalList = new ArrayList<>();
        for(int i = 0; i < 5; i++){
            normalList.add(i);
        }
        ArrayList<Integer>expectedList = new ArrayList<>();
        expectedList.add(0);
        expectedList.add(2);
        expectedList.add(4);
        //When
        ArrayList<Integer>result = exterminator.exterminate(normalList);
        //Then
        Assert.assertEquals(expectedList, result);
    }
}
