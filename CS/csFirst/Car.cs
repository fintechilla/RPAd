using System;

namespace csFirst
{
    public class Car: IEquatable<Car>
    {
        public String Make { get; set; }
        public String Model { get; set; }
        public String Year { get; set; }
        
        //Implementation of IEquitable<T> interface
        public bool Equals(Car car)
        {
            return (this.Make, this.Model, this.Year) == (car.Make, car.Model, car.Year);
        }
        
    }
}