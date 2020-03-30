package com.kod.testing;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import org.sikuli.script.FindFailed;
import org.sikuli.script.Pattern;
import org.sikuli.script.Screen;


public class Hello {
    public static void main(String[] args) throws FindFailed {
        print("Hello World");

        System.setProperty("webdriver.chrome.driver","C:\\Webdrivers\\chromedriver_win32_79_0_3945_130\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();

        String baseUrl = "https://login.salesforce.com/";
        driver.get(baseUrl);

        WebElement elem = driver.findElement(new By.ByCssSelector("#username"));
        elem.sendKeys("User");

        Screen s = new Screen();
        s.wait(2.0);
        System.out.println("Hello a/waiting");

        try  {
            s.find("C:\\Developments\\Java\\Selen\\sample.project\\src\\main\\java\\com\\kod\\testing\\images\\salesforceLogo1043.png");
            System.out.println("Salesforce Logo exists!");
        } catch (FindFailed e){
            System.out.println("FindFailed: Salesforce Logo does not exist" + e.getMessage());
        } finally {
            System.out.println("And going...");
        }

        Pattern p = new Pattern();


    }
    public static void print(String sentence){
        System.out.println(sentence);
    }

}
