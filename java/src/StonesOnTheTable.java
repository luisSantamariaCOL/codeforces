/**
 * https://codeforces.com/problemset/problem/266/A
 *
 * @author SantamariaCOL
 */
import java.util.Scanner;

public class StonesOnTheTable {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        String stones = sc.nextLine();

        int count = 0;
        for (int i = 0; i < stones.length()-1; i++)
            if (stones.charAt(i) == stones.charAt(i+1))
                count++;


        System.out.println(count);
    }
}
