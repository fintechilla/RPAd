package com.kod.stream.world;

import java.math.BigDecimal;

public class Country {
    private BigDecimal population;

    public Country(final BigDecimal population) {
        this.population = population;
    }

    public BigDecimal getCountryPopulation() {
        return population;
    }
}
