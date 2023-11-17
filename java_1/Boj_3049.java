package java_1;

import java.util.Scanner;

public class Boj_3049{
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        // nC4를 구현하면 된다.
        int result = (int)((n * (n - 1) * (n - 2) * (n - 3)) / 24);
        System.out.println(result);

        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_3049().run();
    }
}