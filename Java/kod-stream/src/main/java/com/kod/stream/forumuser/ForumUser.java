package com.kod.stream.forumuser;

import java.time.LocalDate;

public final class ForumUser {
    private final int id;
    private final String name;
    private final char gender;
    private final LocalDate dob;
    private final int noPosts;

    public ForumUser(final int id, final String name, final char gender, final LocalDate dob, final int noPosts) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.dob = dob;
        this.noPosts = noPosts;
    }



    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public char getGender() {
        return gender;
    }

    public LocalDate getDob() {
        return dob;
    }

    public int getNoPosts() {
        return noPosts;
    }

    @Override
    public String toString() {
        return "ForumUser{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", gender=" + gender +
                ", dob=" + dob +
                ", noPosts=" + noPosts +
                '}';
    }
}
