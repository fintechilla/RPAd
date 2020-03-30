package com.kod.stream.invoice.simple;

public class SimpleItem {
    private final SimpleProduct product;
    private final double quantity;

    public SimpleItem(final SimpleProduct product, final double quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    public SimpleProduct getProduct() {
        return product;
    }

    public double getQuantity() {
        return quantity;
    }
    public double getValue(){
        return product.getProductPrice() * quantity;
    }

    @Override
    public String toString() {
        return "SimpleItem{" +
                "product=" + product +
                ", quantity=" + quantity +
                '}';
    }
}
