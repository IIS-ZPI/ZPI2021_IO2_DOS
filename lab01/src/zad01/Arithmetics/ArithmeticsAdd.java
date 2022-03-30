package zad01.Arithmetics;

import zad01.IArithmetics.IArithmeticsAdd;

public class ArithmeticsAdd implements IArithmeticsAdd {

    @Override
    public double Addition(double a, double b) {
        return a + b;
    }
}
