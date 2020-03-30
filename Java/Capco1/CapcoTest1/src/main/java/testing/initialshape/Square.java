package main.java.testing.initialshape;

public class Square implements Shape {
    String shapeName = "Square";
    int w = 3;
    int l = 5;

    public Square() {
    }

    @Override
    public String getShapeName() {
        return this.shapeName;
    }

    @Override
    public double getArea() {
        return this.l * this.w;
    }

    public void soundItOut(){
        System.out.println("Hello this is " + this.shapeName);
    }

}
