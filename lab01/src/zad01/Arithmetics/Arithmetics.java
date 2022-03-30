package zad01.Arithmetics;

import zad01.Arithmetics.Interfaces.IArithmeticsAdd;
import zad01.Arithmetics.Interfaces.IArithmeticsDiff;
import zad01.Arithmetics.Interfaces.IArithmeticsDiv;
import zad01.Arithmetics.Interfaces.IArithmeticsMult;

public class Arithmetics implements IArithmeticsAdd, IArithmeticsDiff, IArithmeticsDiv, IArithmeticsMult {
    //add
    @Override
    public double Addition(double a, double b) {
        return a + b;
    }
    //divide
    @Override
    public double Division(double a, double b) {
        return a / b;
    }
    //subtract
    @Override
    public double Difference(double a, double b) {
        return a - b;
    }
    //multiply
    @Override
    public double Multiplication(double a, double b) {
        return a * b;
    }
}
