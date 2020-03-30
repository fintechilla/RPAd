using System;

namespace csFirst
{
    class Program
    {
        private const string Value = "Type in a 2nd number and press Return";

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            // int a = 42;
            // int b = 119;
            // int c = a + b;43
            // Console.WriteLine(c);
            // Console.Read();
            int num1 = 0; int num2 = 0;
            String num1s = ""; String num2s = "";
            String beautifier = "******";
            Console.WriteLine("Console Calculator in C#\r");
            Console.WriteLine("-------------------------");
            Console.WriteLine("Type in a 1st number and press Return");
            num1s = Console.ReadLine();
            Console.WriteLine($"You entered: {num1s}");
            Console.WriteLine("Type in a 2nd number and press Return");
            num2s = Console.ReadLine();
            Console.WriteLine($"{beautifier}You entered 2 number: {num2s}{beautifier}");
            num1 = Convert.ToInt32(num1s);
            num2 = Convert.ToInt32(num2s);
            int total = num1 + num2;
            Console.WriteLine($"{beautifier}The sum of {num1s} and {num2s} is = {total}{beautifier}");

        }
    }
}
