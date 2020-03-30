package main.java.play;

public class Geek {

    int num;
    String name;

    // this would be invoked while an object
    // of that class is created.
    Geek()
    {
        System.out.println("Constructor called");
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
