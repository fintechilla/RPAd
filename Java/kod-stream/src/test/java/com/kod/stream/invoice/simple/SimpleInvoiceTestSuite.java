package com.kod.stream.invoice.simple;

import org.junit.Assert;
import org.junit.Test;

public class SimpleInvoiceTestSuite {
    @Test
    public void testGetValueToPay(){
        //Assume
        SimpleInvoice invoice = new SimpleInvoice();
        //Action
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 1", 17.28), 2.0001));
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 2", 11.99), 3.50));
        invoice.addItem(new SimpleItem(new SimpleProduct("Product 3", 6.49), 5.0));
        invoice.printInvoice();
        //Assert
        Assert.assertEquals(108.975, invoice.getValueToPay(), 0.01);

    }
}
