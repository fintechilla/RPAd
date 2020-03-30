package com.kod.stream.lambda;

public class ExecuteSaySomething implements Executor {
    @Override
    public void process() {
        System.out.println("ExecuteSaySomething: This is an example text");
    }
}
