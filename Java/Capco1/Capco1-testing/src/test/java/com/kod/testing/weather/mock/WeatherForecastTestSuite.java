package com.kod.testing.weather.mock;
import com.kod.testing.weather.stub.Temperatures;
import com.kod.testing.weather.stub.WeatherForecast;
import org.junit.Assert;
import org.junit.Test;

import java.util.HashMap;

import static org.mockito.Mockito.*;


public class WeatherForecastTestSuite {
    @Test
    public void testCalculateForecastWithMock(){
        //Assume
        Temperatures temperaturesMock = mock(Temperatures.class);
        HashMap<Integer, Double> temperaturesMap = new HashMap<>();
        temperaturesMap.put(0, 25.5);
        temperaturesMap.put(1, 26.2);
        temperaturesMap.put(2, 24.2);
        temperaturesMap.put(3, 25.2);
        temperaturesMap.put(4, 27.2);
        when(temperaturesMock.getTemperatures()).thenReturn(temperaturesMap);
        WeatherForecast forecast = new WeatherForecast(temperaturesMock);
        //Action
        int quantityOfSensors = forecast.calculateForecast().size();
        //Assert
        Assert.assertEquals(5, quantityOfSensors);
    }
}
