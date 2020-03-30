package com.kod.stream;

import com.kod.stream.book.Book;
import com.kod.stream.book.BookDirectory;
//import com.kod.stream.immutable.BookDirectory;
import com.kod.stream.forumuser.Forum;
import com.kod.stream.forumuser.ForumUser;
import com.kod.stream.immutable.NumbersGenerator;
import com.kod.stream.invoice.simple.SimpleInvoice;
import com.kod.stream.invoice.simple.SimpleItem;
import com.kod.stream.invoice.simple.SimpleProduct;
import com.kod.stream.lambda.*;
import com.kod.stream.person.People;

import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.time.temporal.ChronoUnit;

public class StreamMain {
    public static <intervalPeriod> void main(String[] args) {
        System.out.println("******************Welcome to Stream - 7 ***********************");
        Processor processor = new Processor();
        ExecuteSaySomething executeSaySomething = new ExecuteSaySomething();
        processor.execute(executeSaySomething);
        Executor codeToExecute = () -> System.out.println("codeToExecute: Hello");
        processor.execute(codeToExecute);

        System.out.println("expressionExecutor.executeExpression(10, 5, (a, b)-> a+b); - calculating expressions with lambdas*********");
        ExpressionExecutor expressionExecutor = new ExpressionExecutor();
        expressionExecutor.executeExpression(10, 5, (a, b)-> a+b);
        expressionExecutor.executeExpression(10, 5, (a, b)-> a-b);
        expressionExecutor.executeExpression(10, 5, (a, b)-> a*b);
        expressionExecutor.executeExpression(10, 5, (a, b)-> a/b);

        System.out.println("Method reference - FunctionalCalculator - Calculating expressions with method references******************");

        expressionExecutor.executeExpression(10, 5, FunctionalCalculator::addAToB);
        expressionExecutor.executeExpression(10, 5, FunctionalCalculator::subBFromA);
        expressionExecutor.executeExpression(10, 5, FunctionalCalculator::multiplyAByB);
        expressionExecutor.executeExpression(10, 5, FunctionalCalculator::divideAByB);

        System.out.println("Using Stream to generate even numbers from 1 to 20");
        NumbersGenerator.generateEven(20);

        People.getList().stream()
                .forEach(System.out::println);
//        System.out.println("The book list *************");
//        People.getList().stream().map(s->s.toUpperCase()).forEach(System.out::println);
//        People.getList().stream().map(String::toLowerCase).forEach(System.out::println);
//        System.out.println("Names longer than 11 chars*************");
//        People.getList().stream().filter(s->s.length()>11).forEach(System.out::println);
//        System.out.println("several filters***********");
//        People.getList().stream().map(String::toUpperCase)
//                .filter(s->s.length()> 11)
//                .map( s->s.substring(0, s.indexOf(' ')+2)+".")
//                .filter(s->s.substring(0,1).equals("M"))
//                .forEach(System.out::println);

        System.out.println("BookDirectory as a Map************");
        BookDirectory theBookDirectory = new BookDirectory();
        theBookDirectory.getTheBookList().stream()
                .filter(book->book.getYearOfPublication() > 2005)
                .collect(Collectors.toList())
                .forEach(System.out::println);

        Map<String, Book>theResultMapOfBooks = theBookDirectory.getTheBookList().stream()
                .filter(book->book.getYearOfPublication() > 2005)
                .collect(Collectors.toMap(Book::getSignature, book->book));
        System.out.println("# elements: " + theResultMapOfBooks.size());
        theResultMapOfBooks.entrySet().stream()
                .map(entry->entry.getKey() + ": " + entry.getValue())
                .forEach(System.out::println);
        System.out.println("Collectors.joining*************");
        String theResultStringOfBooks = theBookDirectory.getTheBookList().stream()
                .filter(book->book.getYearOfPublication() > 2005)
                .map(Book::toString)
                .collect(Collectors.joining(",\n", "<<", ">>"));
        System.out.println("theResultStringOfBooks: " +  theResultStringOfBooks);

        System.out.println("The ForumUser************ ");
        Forum forum = new Forum();
        List<ForumUser> theFUList = forum.getUserList();
        int nPosts = 2;
        int nYears = 15;
        LocalDate cDate = LocalDate.now();      //of(2020, 03, 17);
        Period  intervalPeriod;
        Map<Integer, ForumUser> mapList = theFUList.stream()
                .filter(s->s.getNoPosts() > nPosts)
                .filter(s->s.getGender() == 'M')
                .filter(s->ChronoUnit.YEARS.between(s.getDob(), cDate) > nYears )
//                .map(s->s.toString())
                .collect(Collectors.toMap(ForumUser::getId, ForumUser-> ForumUser));
        System.out.println("Printing entry sets from map++++");
        mapList.entrySet().stream()
                .map(entry -> entry.getKey() + ": " + entry.getValue())
                .forEach(s->System.out.println(s));

        System.out.println("Simple Invoice ***************");
        //Assume
        SimpleInvoice invoice = new SimpleInvoice();
        //Action
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 1", 17.28), 2.0));
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 2", 11.99), 3.50));
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 3", 6.49), 5.0));
        invoice.printInvoice();

    }

}
