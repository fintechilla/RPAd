package com.kod.stream.invoice.simple;

import java.util.Objects;

public class SimpleProduct {
    private final String productName;
    private final double productPrice;

    public SimpleProduct(final String productName, final double productPrice) {
        this.productName = productName;
        this.productPrice = productPrice;
    }

    public String getProductName() {
        return productName;
    }

    public double getProductPrice() {
        return productPrice;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof SimpleProduct)) return false;
        SimpleProduct that = (SimpleProduct) o;
        return getProductName().equals(that.getProductName());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getProductName());
    }

    @Override
    public String toString() {
        return "SimpleProduct{" +
                "productName='" + productName + '\'' +
                ", productPrice=" + productPrice +
                '}';
    }
}
