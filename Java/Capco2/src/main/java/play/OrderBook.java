package main.java.play;

import java.util.HashSet;

public class OrderBook {

    private HashSet<Order> orderSet; // = new HashSet<String>();

    OrderBook(){
        System.out.println("Constructor called");
        this.orderSet = new HashSet<Order>();
    }

    public void addOrder(Order order){
        this.orderSet.add(order);
    }

    public void  printOrders(){
        for (Order entry : this.orderSet) {
            System.out.println(entry.getNum() + " " + entry.getTitle());
        }
    }

    public HashSet<Order> getOrderSet() {
        return orderSet;
    }

    public void setOrderSet(HashSet<Order> orderSet) {
        this.orderSet = orderSet;
    }

    @Override
    public String toString() {
        return "OrderBook{" +
                "orderSet=" + orderSet +
                '}';
    }
}

