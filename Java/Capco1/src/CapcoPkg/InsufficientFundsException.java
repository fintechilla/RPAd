package CapcoPkg;
import java.io.*;
public class InsufficientFundsException extends Exception{

    // File Name InsufficientFundsException.java

    private double amount;

    public InsufficientFundsException(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }
}
