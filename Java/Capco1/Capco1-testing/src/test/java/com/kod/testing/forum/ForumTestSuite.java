package com.kod.testing.forum;
import com.kod.testing.user.SimpleUser;
import org.junit.*;

public class ForumTestSuite {
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
    private static int testCounter = 0;


    @Test
    public void testCaseUsername(){
        //Given
        SimpleUser simpleUser = new SimpleUser("theForumUser", "John Miller");
        //When
        String result = simpleUser.getUsername();
        //Then
        Assert.assertEquals("theForumUser", result);
    }
    @Test
    public void testCaseRealName(){
        //Given
        SimpleUser simpleUser = new SimpleUser("theForumUser", "John Miller");
        //When
        String result = simpleUser.getRealName();
        //Then
        Assert.assertEquals("John Miller", result);
    }



}
