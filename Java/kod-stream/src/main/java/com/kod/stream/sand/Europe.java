package com.kod.stream.sand;

import java.math.BigDecimal;

public final class Europe implements SandStorage {

    @Override
    public BigDecimal getSandBeansQuantity() {
        BigDecimal sandQantity = new BigDecimal("12345678901234567890");
        return sandQantity;
    }
}
