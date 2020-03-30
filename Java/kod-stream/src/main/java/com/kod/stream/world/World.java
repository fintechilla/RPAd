package com.kod.stream.world;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class World {
    private List<Continent>continentList = new ArrayList<>();

    public World() {

    }
    public void addContinents(Continent continent){
        continentList.add(continent);
    }
    public List<Continent> getContinentList() {
        return continentList;
    }
    public BigDecimal getWorldPopulation(){
        BigDecimal result = continentList.stream()
                .flatMap(continent->continent.getCountryList().stream())
                .map(country -> country.getCountryPopulation())
                .reduce(BigDecimal.ZERO, (sum, current)->sum.add(current));
        return result;
    }
}
