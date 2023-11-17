package java_1;

import java.util.*;

public class Boj_9625{
    public void run()
    {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int a = 0;
        int b = 1;

        for(int i = 1 ; i < n ; i++)
        {
            int temp = a;
            a = b;
            b = temp + b;
        }

        System.out.println(String.format("%d %d" , a , b));
    
        scan.close();
    }

    public static void main(String[] args)
    {
        new Boj_9625().run();
    }
}