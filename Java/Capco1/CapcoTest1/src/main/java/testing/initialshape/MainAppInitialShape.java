package main.java.testing.initialshape;
import java.lang.String;

public class MainAppInitialShape {
    public static void main(String[] args){
        Shape shape;
        shape = new Circle();
        Circle circle = new Circle();
        String circleSound = String.format("circle.sound(): %1$s", circle.sound());
        System.out.println(circleSound);

        ShapeTeller teller = new ShapeTeller(shape) ;
        teller.executeName();
        teller.executeArea();

        shape = new Square();
        Square square = new Square();
        square.soundItOut();
        teller = new ShapeTeller(shape) ;
        teller.executeName();
        teller.executeArea();
    }
}
