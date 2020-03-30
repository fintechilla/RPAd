package com.kod.testing.forum;

import java.util.Objects;

public class ForumPost {
    String postBody;
    String author;

    public ForumPost(String postBody, String author) {
        this.postBody = postBody;
        this.author = author;
    }

    public String getPostBody() {
        return postBody;
    }

    public void setPostBody(String postBody) {
        this.postBody = postBody;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof ForumPost)) return false;
        ForumPost forumPost = (ForumPost) o;
        return Objects.equals(getPostBody(), forumPost.getPostBody()) &&
                Objects.equals(getAuthor(), forumPost.getAuthor());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getPostBody(), getAuthor());
    }
}
