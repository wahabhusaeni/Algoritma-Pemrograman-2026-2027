import java.util.Locale;
import java.util.Scanner;
 
public class coba2 {
    public static void main(String[] args) {
        var in = new Scanner(System.in).useLocale(Locale.US);
 
        System.out.print("Input alas   : ");
        double alas = in.nextDouble();
        System.out.print("Input tinggi : ");
        double tinggi = in.nextDouble();
 
        double luas = alas * tinggi / 2;
        System.out.printf(Locale.US, "Luas segitiga adalah %.2f%n", luas);
    }
}