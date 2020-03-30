package main.java.play;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

class Order {

    private Integer num;
    private String title;

    public Order(Integer num, String title) {
        this.num = num;
        this.title = title;
    }
    public Integer getNum() {
        return num;
    }

    public void setNum(Integer num) {
        this.num = num;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}
