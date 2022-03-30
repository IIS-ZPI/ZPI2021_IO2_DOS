package zad01;

import zad01.IArithmetics.IArithmeticsDiff;

public class ArithmeticsDiff implements IArithmeticsDiff {
    @Override
    public double Difference(double a, double b) {
        return a - b;
    }
}
