package com.kod.testing.weather.stub;


import org.junit.Assert;
import org.junit.Test;

public class TestWeatherForecastTestSuite {

    @Test
    public void testCalculateForecastWithStub(){
        //Assume
        Temperatures temperatures = new TemperaturesStub();
        WeatherForecast forecast = new WeatherForecast(temperatures);
        //Action
        int quantityOfSensors = forecast.calculateForecast().size();
        //Assert
        Assert.assertEquals(5, quantityOfSensors);

    }

}
