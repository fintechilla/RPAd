package main.java.play;
import java.util.*;
import java.util.stream.*;

public class mainApp {

    public static void main(String[] args){
        Map <Integer,String> myFavoriteColors = new HashMap <Integer,String> ();
        Map <Integer,String> myFriendsFavoriteColors = new HashMap <Integer,String> ();

        myFavoriteColors.put(1, "Red");
        myFavoriteColors.put(2, "Green");
        myFavoriteColors.put(3, "Black");
        System.out.println("Values in first map: " + myFavoriteColors);
        myFriendsFavoriteColors.put(4, "White");
        myFriendsFavoriteColors.put(5, "Blue");
        myFriendsFavoriteColors.put(6, "Orange");
        System.out.println("Values in second map: " + myFriendsFavoriteColors);

        Map <Integer,String> ourFavoriteColors = new HashMap <Integer,String> ();

        for (Map.Entry<Integer, String> entry: myFavoriteColors.entrySet()){
            ourFavoriteColors.put(entry.getKey(), entry.getValue());
        }
        for (Map.Entry<Integer, String> entry: myFriendsFavoriteColors.entrySet()){
            ourFavoriteColors.put(entry.getKey(), entry.getValue());
        }
        System.out.println("Values in third map: " + ourFavoriteColors);
        for(Map.Entry<Integer, String> entry : ourFavoriteColors.entrySet()){
            System.out.println(entry);
        }

        // this would invoke default constructor.
        Geek geek1 = new Geek();

        // Default constructor provides the default
        // values to the object like 0, null
        System.out.println(geek1.name);
        System.out.println(geek1.num);
        geek1.setName("John");
        geek1.setNum(5);
        System.out.println(geek1.getName());
        System.out.println(geek1.getNum());


//        HashSet<String>mySet = null;
        OrderBook orders = new OrderBook();
        System.out.println(orders.getOrderSet());
//        orders.setOrderSet(mySet);
        Order order1 = new Order(1, "pizza");
        Order order2 = new Order(1, "pizza");
        Order order3 = new Order(2, "pizza");
        Order order4 = new Order(2, "kebab");
        Order order5 = new Order(3, "steak");

        orders.addOrder(order1);
        orders.addOrder(order2);
        orders.addOrder(order3);
        orders.addOrder(order4);
        orders.addOrder(order5);

        orders.printOrders();

        List<Integer>numbers = Arrays.asList("2, 3, 4, 5");
        List<Integer>squares = numbers.stream()
                .map(x -> x*x)
                .forEach(y -> System.out.println(y));






    }
}
