package com.kod.testing;

import com.kod.testing.user.SimpleUser;
import com.kod.testing.Calculator;

public class testingMain {

    public static void main(String[] args){
        System.out.println("Modul 6. Wprowadzenie to testowania oprogramowania");

        SimpleUser simpleUser = new SimpleUser("theForumUser", "John Miller");

        String result = simpleUser.getUsername();

        if (result.equals("theForumUser")){
            System.out.println("test OK");
        } else {
            System.out.println("Error!");
        }

        Calculator calculator = new Calculator();
        int resultAdd = calculator.add(1, 3);
        int resultSub = calculator.subtract(3, 5);

        System.out.println(resultAdd + " " + resultSub);











    }
}
