package main.java.testing.initialshape;

public class Circle implements Shape{
    public String shapeName = "Circle";
    private int r = 3;

    public Circle() {
    }


    @Override
    public String getShapeName() {
        return this.shapeName;
    }

    @Override
    public double getArea() {
        return 3.14159*r;
    }

    public String sound(){
        return "From outside of interface: " + this.shapeName;
    }
}
