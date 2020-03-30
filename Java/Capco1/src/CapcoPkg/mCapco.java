package CapcoPkg;

import javax.annotation.processing.Completion;
import javax.annotation.processing.ProcessingEnvironment;
import javax.annotation.processing.Processor;
import javax.annotation.processing.RoundEnvironment;
import javax.lang.model.SourceVersion;
import javax.lang.model.element.AnnotationMirror;
import javax.lang.model.element.Element;
import javax.lang.model.element.ExecutableElement;
import javax.lang.model.element.TypeElement;
import java.sql.Time;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;
import java.util.*;
import java.util.concurrent.Executor;


public class mCapco {

    public static void main(String[] args) {
        List<String> listA = new ArrayList<>();
        listA.add("One");
        listA.add("Two");
        listA.add("Three");

        int i = 0;
        System.out.println("ListA:");
        for (String item : listA) {
            System.out.println(((Integer) i) + item);
            i += 1;
        }

        System.out.println(listA.get(1));

        listA.add(1, "Four");
        System.out.println("ListA:");
        for (String item : listA) {
            System.out.println(item);
        }

        LinkedList<String> listB = new LinkedList<>();

        listB.add("One");
        listB.add("Two");
        listB.add("Three");
        System.out.println("ListB:");

        for (String item : listB) {
            System.out.println(item);
        }
        listB.add(2, "Four");
        System.out.println("ListB:");

        for (String item : listB) {
            System.out.println(item);
        }

        Locale locale = new Locale("en", "US");
        DateFormat dateFormat = DateFormat.getDateInstance(DateFormat.DEFAULT, locale);
        String date = dateFormat.format(new Date());
        System.out.print(date + "\n");

        String pattern = "HH:mm:ss.SSSZ";
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern);
        date = simpleDateFormat.format(new Date());
        System.out.println(date);


        Employee e1 = new Employee("John", "Miller", "001");
        Employee e2 = new Employee("John1", "Miller1", "0011");
        Employee e3 = new Employee("John", "Miller", "001");
        System.out.println("e1: " + e1.firstName.toString());
        System.out.println(e1.equals(e3));

        HashMap<Integer, String> theMap = new HashMap<Integer, String>();
        theMap.put(1, "One");
        theMap.put(2, "Two");
        theMap.put(7, "Seven");

        System.out.println("Using entrySet() to retrieve and display content of the map");
        for (Map.Entry<Integer, String> entry : theMap.entrySet()) {
            System.out.println("Object: <" + entry.getKey() + ", " + entry.getValue() + ">");
        }

        SimpleDateFormat formatter= new SimpleDateFormat("yyyy-MM-dd '@' HH:mm:ss z");
        long date0 = System.currentTimeMillis();
        System.out.println("date0 in millis: " + date0);
        Date date1 = new Date(date0);
        System.out.println("Date date1 as formatted date0: " + formatter.format(date1));


        System.out.println("Date date1: " + date1);
        long date2 = System.currentTimeMillis();
        System.out.println("formatter(date2): " + formatter.format(date2));

        System.out.println("Time diff: " + (date2 - date0));

        LocalTime time = LocalTime.now();
        System.out.println("local time no formatting: " + time);

        AnimalRecognizer recognizer = new AnimalRecognizer(new Cat());
        String recognizedAnimal;
        recognizedAnimal = recognizer.recognize(new Cat());
        System.out.println(recognizedAnimal);

        recognizedAnimal = recognizer.recognize(new Dog());
        System.out.println(recognizedAnimal);

        System.out.println("class: " + Dog.class);

        System.out.println("InsufficientAccountException +++");
        System.out.println("++++++++++++++++++++++++++++++++++++");

        CheckingAccount c = new CheckingAccount(101);
        System.out.println("Depositing $500...");
        c.deposit(500.00);

        try {
            System.out.println("\nWithdrawing $100...");
            c.withdraw(100.00);
            System.out.println("\nWithdrawing $600...");
            c.withdraw(600.00);
        } catch (InsufficientFundsException e) {
            System.out.println("Sorry, but you are short $" + e.getAmount());
            e.printStackTrace();
        }
        finally {
            System.out.println("EOP");
        }

        System.out.println("Keep going!");

        HashSet<Employee> wSet = new HashSet<>();

        wSet.add(e1);
        wSet.add(e2);
        wSet.add(e1);
        wSet.add(e3);

        System.out.println(wSet.size());
        for(Employee employee:wSet){
            System.out.println(employee.toString());
        }
    }
}

