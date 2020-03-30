package com.kod.stream.forumuser;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public final class Forum {
     private final List<ForumUser>theList = new ArrayList<>();

    public Forum() {
        theList.add(new ForumUser(1, "John", 'M', LocalDate.of(2000, 05, 20), 4));
        theList.add(new ForumUser(2, "Mary", 'F', LocalDate.of(1990, 05, 20), 14));
        theList.add(new ForumUser(3, "Marcy", 'F', LocalDate.of(2004, 05, 20), 4));
        theList.add(new ForumUser(4, "Mandy", 'F', LocalDate.of(2006, 05, 20), 16));
        theList.add(new ForumUser(5, "Marlon", 'M', LocalDate.of(1972, 05, 20), 14));
        theList.add(new ForumUser(6, "Mike", 'M', LocalDate.of(1984, 05, 20), 2));
        theList.add(new ForumUser(7, "Adam", 'M', LocalDate.of(1959, 05, 20), 10));
        theList.add(new ForumUser(8, "Dana", 'F', LocalDate.of(1986, 05, 20), 13));
    }

    public List<ForumUser> getUserList() {
        return new ArrayList<ForumUser>(theList) ;
//        return theList;
    }

    @Override
    public String toString() {
        return "Forum{" +
                "theList=" + theList +
                '}';
    }
}
