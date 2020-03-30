package CapcoPkg;

public class AnimalRecognizer {
    Animal animal;
    public String recognize(Animal animal){
        return "I am a " + animal.name() + " and I sound like " + animal.voice();
    }

    public AnimalRecognizer(Animal animal) {
        this.animal = animal;
    }
}
