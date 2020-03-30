package FirstPackage;
import java.util.Iterator;
import java.util.List;

import org.openqa.selenium.WebDriver;
import org.sikuli.script.Match;
import org.sikuli.script.Screen;
import org.openqa.selenium.chrome.ChromeDriver;

public class testWeb {
    public static void main(String[] args){
        System.out.println("Hello World");

        System.setProperty("webdriver.chrome.driver", "C:\\Users\\p2881790\\Desktop\\Webdrivers\\chromedriver_win32_75_0_3770_140\\chromedriver.exe");
        System.out.println("b/opening chrome");
        System.out.println(System.getProperties());
        WebDriver driver = new ChromeDriver();
        System.out.println("a/opening chrome");

        String baseUrl = "https://login.salesforce.com/";

        driver.get(baseUrl);
        String actualTitle = driver.getTitle();

        System.out.println(actualTitle);



    }
}
