package com.kod.stream.invoice.simple;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class SimpleInvoice {
    private final List<SimpleItem>items = new ArrayList<>();

    public void addItem(SimpleItem item){
        items.add(item);
    }
    public boolean removeItem(SimpleItem item){
        return items.remove(item);
    }
    public double getValueToPay(){
        return items.stream()
                .collect(Collectors.summingDouble(SimpleItem::getValue));
    }
    public void printInvoice(){
        items.stream()
                .map(item->item.toString() + " = " + item.getValue())
                .forEach(System.out::println);
    }

    @Override
    public String toString() {
        return "SimpleInvoice{" +
                "items=" + items +
                '}';
    }
}
