package com.kod.stream.sand;

import java.math.BigDecimal;

public final class Asia implements SandStorage {
    @Override
    public BigDecimal getSandBeansQuantity() {
        BigDecimal sanQuantity = new BigDecimal("98765432101234567890");
        return sanQuantity;
    }
}
