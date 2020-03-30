package CapcoPkg;

public class Cat implements Animal {

    @Override
    public String voice() {
        return "Miau Miau";
    }

    @Override
    public String name() {
        return "Cat!";
    }
}
