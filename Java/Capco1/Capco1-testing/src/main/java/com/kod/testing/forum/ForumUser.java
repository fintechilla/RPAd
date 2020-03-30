package com.kod.testing.forum;
import java.util.ArrayList;
import java.util.LinkedList;

public class ForumUser {
    private String name;
    private String realName;
    private ArrayList<ForumPost> posts = new ArrayList<ForumPost>();
    private LinkedList<ForumComment> comments = new LinkedList<ForumComment>();

    public ForumUser(String name, String realName) {
        //name visible on forum
        this.name = name;
        //real name of the user
        this.realName = realName;
    }
    public void addPost(String author, String postBody){
        // do nothing
        posts.add(new ForumPost(postBody, author));
    }

    public void addComment(ForumPost thePost, String author, String commentBody){
        // do nothing
        comments.add(new ForumComment(thePost, commentBody, author));
    }

    public int getPostsQuantity(){
         return posts.size();
    }

    public int getCommentsQuantity(){
        // return 100 temporarily
        return comments.size();
    }

    public ForumPost getPost(int postNumber){
        // returning null means that the operation was unsuccessful
        return posts.get(postNumber);
    }

    public ForumComment getComment(int commentNumber){
        // returning null means that the operation was unsuccessful
        return comments.get(commentNumber);
    }

    public boolean removePost(ForumPost thePost){
        // return true temporarily
        return posts.remove(thePost);
    }

    public boolean removeComment(ForumComment theComment){
        // return true temporarily
        return comments.remove(theComment);
    }

    public String getName() {
        return name;
    }

    public String getRealName() {
        return realName;
    }
}


