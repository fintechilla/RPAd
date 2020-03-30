package CapcoPkg;

import java.util.Objects;

public class Employee {
    String firstName;
    String lastName;
    String pslId;

//    public Employee(String john, String miller, String s) {
//    }
    public Employee(String firstName, String lastName, String pslId){
        this.firstName = firstName;
        this.lastName = lastName;
        this.pslId = pslId;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", pslId='" + pslId + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Employee)) return false;
        Employee employee = (Employee) o;
        return firstName.equals(employee.firstName) &&
                lastName.equals(employee.lastName) &&
                pslId.equals(employee.pslId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(lastName);
    }





}
