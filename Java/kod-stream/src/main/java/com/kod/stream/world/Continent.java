package com.kod.stream.world;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class Continent {
    private List<Country>countryList = new ArrayList<>();

    public Continent(final List<Country> countryList) {
        this.countryList = countryList;
    }
    public void addCountry(Country country){
        countryList.add(country);
    }

    public List<Country> getCountryList() {
        return countryList;
    }
    public BigDecimal getContinentPopulation(){
        return countryList.stream().map(Country::getCountryPopulation)
                .reduce(BigDecimal.ZERO, (sum, current)->sum.add(current));
    }
}
