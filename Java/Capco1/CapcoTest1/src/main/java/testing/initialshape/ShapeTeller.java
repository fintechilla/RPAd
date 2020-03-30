package main.java.testing.initialshape;

public class ShapeTeller {

    Shape shape;

    public ShapeTeller(Shape shape) {
        this.shape = shape;
    }

    void executeName(){
        System.out.println(shape.getShapeName());
    }
    void executeArea(){
        System.out.println(shape.getArea());
    }
}
