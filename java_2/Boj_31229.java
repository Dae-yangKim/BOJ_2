package java_2;

import java.util.Scanner;

public class Boj_31229{
    public void run()
    {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        for(int i = 1 ; i < n ; i++)
        {
            System.out.print((2 * i - 1) + " ");
        }

        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_31229().run();
    }
}