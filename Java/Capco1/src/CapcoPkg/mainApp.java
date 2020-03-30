package CapcoPkg;

public class mainApp {
    public static void main(String[] args){
        Cat cat = new Cat();
        AnimalRecognizer recognizer = new AnimalRecognizer(cat);
        recognizer.recognize(cat);

    }
}
