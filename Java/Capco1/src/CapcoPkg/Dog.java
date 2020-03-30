package CapcoPkg;

public class Dog implements Animal {
    @Override
    public String voice() {
        return "Hau Hau";
    }

    @Override
    public String name() {
        return "Dog!";
    }
}
