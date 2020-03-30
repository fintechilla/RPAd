package com.kod.testing.forum.tdd;

import com.kod.testing.forum.ForumComment;
import com.kod.testing.forum.ForumPost;
import com.kod.testing.forum.ForumUser;
//import com.sun.org.apache.xpath.internal.functions.FuncFalse;
import org.junit.*;

import javax.xml.stream.FactoryConfigurationError;

public class ForumTestSuite {
    private static int testCounter = 0;
    private static String initialPost = "this is my contribution here!";
    private static String thanksComment = "Thank you for all good words!";

    @BeforeClass
    public static void beforeAllTests(){
        System.out.println("This is the beginning of tests");
    }
    @AfterClass
    public static void afterAllTests(){
        System.out.println("All " + testCounter + " tests are finished");
    }
    @Before
    public void beforeEveryTest(){
        testCounter ++;
        System.out.println("Preparing to execute test#: " + testCounter);
    }
    @Test //1
    public void testAddPost(){
        //Given
        ForumUser forumUser = new ForumUser("mrsmith", "John Smith");
        //When
        forumUser.addPost("mrsmith", "Hello everyone, this is my contribution here!");
        //Then
        Assert.assertEquals(1, forumUser.getPostsQuantity());
    }
    @Test //2
    public void testAddComment(){
        //Given
        ForumUser forumUser = new ForumUser("mrsmith", "John Smith");
        ForumPost forumPost = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
//        ForumComment comment = new ForumComment(forumPost, thanksComment, forumUser.getName());
        //When
        forumUser.addComment(forumPost, thanksComment, forumUser.getName());
        //Then
        Assert.assertEquals(1, forumUser.getCommentsQuantity());
    }
    @Test //3
    public void testGetPost(){
        //Given
        ForumUser forumUser = new ForumUser("mrsmith", "John Smith");
        ForumPost forumPost = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
        forumUser.addPost(forumPost.getAuthor(), forumPost.getPostBody());
        //When
        ForumPost retrievedPost;
        retrievedPost = forumUser.getPost(0);
        //Then
        Assert.assertEquals(forumPost, retrievedPost);
    }
    @Test //4
    public void testGetComment(){
        //Given
        ForumUser user = new ForumUser("mrsmith", "John Smith");
        ForumPost post = new ForumPost("Helllo everyone, " + initialPost, user.getName());
        ForumComment comment = new ForumComment(post, user.getName(), thanksComment);
        user.addComment(post, comment.getAuthor(), comment.getCommentBody());
        //When
        ForumComment retrievedComment = user.getComment(0);
        //Then
        Assert.assertEquals(comment, retrievedComment);
        // Assert.assertEquals(null, retrievedComment);
    }
    @Test //5
    public void testRemovePostNotExisting(){
        //Given
        ForumUser user = new ForumUser("mrsmith", "John Smith");
        ForumPost post = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
        //When
        boolean result = user.removePost(post);
        //Then
        Assert.assertFalse(result);  //result
    }
    @Test //6
    public void testRemoveCommentNotExisting(){
        //Given
        ForumUser user = new ForumUser("mrsmith", "John Smith");
        ForumPost post = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
        ForumComment comment = new ForumComment(post, user.getName(), thanksComment);
        //When
        boolean result = user.removeComment(comment);
        //Then
        Assert.assertFalse(result);  //result
    }

    @Test //7
    public void testRemovePost(){
        //Given
        ForumUser user = new ForumUser("mrsmith", "John Smith");
        ForumPost post = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
        user.addPost(post.getAuthor(), post.getPostBody());
        //When
        boolean result = user.removePost(post);
        //Then
        Assert.assertTrue(result);
        Assert.assertEquals(0, user.getPostsQuantity());
    }
    @Test //8
    public void testRemoveComment(){
        //Given
        ForumUser user = new ForumUser("mrsmith", "John Smith");
        ForumPost post = new ForumPost("Hello everyone, " + initialPost, "mrsmith");
        ForumComment comment = new ForumComment(post, user.getName(), thanksComment);
        user.addComment(post, comment.getAuthor(), comment.getCommentBody());
        //When
        boolean result = user.removeComment(comment);
        //Then
        Assert.assertTrue(result);
        Assert.assertEquals(0, user.getCommentsQuantity());

    }
}
