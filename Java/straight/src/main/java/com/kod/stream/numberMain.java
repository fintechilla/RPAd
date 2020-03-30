package com.kod.stream;
import java.util.*;
import java.util.stream.*;

public class numberMain {
    public void main(String[] args){
        List<Integer>numbers = Arrays.asList(2, 3, 4, 5);
        List<Integer>squares = numbers.stream()
                .map(x -> x*x)
                .collect(Collectors.toList());

        squares.stream().forEach(y -> System.out.println(y));
    }
}
