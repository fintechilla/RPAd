//package com.kod.stream.forum;
//
//import java.util.ArrayList;
//import java.util.List;
//import java.util.Objects;
//import java.util.Set;
//import java.util.stream.Collectors;
//
//public class Forum {
//    private final List<ForumUser> friends = new ArrayList<>();
//
//
//    public Forum() {
//    }
//    public void addFriend(com.kod.stream.forum.ForumUser user){
//        friends.add(user);
//    }
//    public boolean removeFriend(com.kod.stream.forum.ForumUser user){
//        return friends.remove(user);
//    }
//    public Set<String> getLocationsOfFriends(){
//        return friends.stream()
//                .map(friend->friend.getLocation())
//                .collect(Collectors.toSet());
//    }
//
//    @Override
//    public boolean equals(Object o) {
//        if (this == o) return true;
//        if (!(o instanceof Forum)) return false;
//        Forum forum = (Forum) o;
//        return friends.equals(forum.friends);
//    }
//
//    @Override
//    public int hashCode() {
//        return Objects.hash(friends);
//    }
//
//    @Override
//    public String toString() {
//        return "Forum{" +
//                "friends=" + friends +
//                '}';
//    }
//}
