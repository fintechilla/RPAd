package com.kod.stream.immutable;

import java.util.ArrayList;
import java.util.List;

public final class BookDirectory {
    private final List<Book>theBookList = new ArrayList<>();

    public BookDirectory() {
        theBookList.add(new Book("Dylan Murphy", "Wolf of the mountains", 2003));
        theBookList.add(new Book("Phoebe Pearson", "Slaves of dreams", 2012));
        theBookList.add(new Book("Morgan Walsh", "Obliteration of heaven", 2001));
        theBookList.add(new Book("Aimee Murphy", "Rejecting the night", 2015));
        theBookList.add(new Book("Ryan Talley", "Gangsters and kings", 2007));
        theBookList.add(new Book("Madelynn Carson", "Unity without duty", 2007));
        theBookList.add(new Book("Giancarlo Guerrero", "Enemies of eternity", 2009));

    }

    public List<Book> getList() {
        return new ArrayList<>(theBookList);
    }
}
