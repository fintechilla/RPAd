package com.kod.testing.collection;

import java.util.ArrayList;

public class OddNumbersExterminator {

    public OddNumbersExterminator() {
    }

    public ArrayList<Integer> exterminate(ArrayList<Integer>numList){
        ArrayList<Integer> tempList = new ArrayList<>();

        if (numList == null){
            return null;
        }
        System.out.println("OddNumberExterminator:non null:exterminate:begin");
        for (Integer num : numList) {
            if (num % 2 == 0){
                tempList.add(num);
            }

        }
        return tempList;

    }
}
