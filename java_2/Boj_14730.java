package java_2;

import java.util.Scanner;

public class Boj_14730{
    public void run()
    {
        Scanner s = new Scanner(System.in);

        int n = s.nextInt();
        int result = 0;

        for(int i = 0 ; i < n ; i++)
        {
            int c = s.nextInt();
            int k = s.nextInt();

            result += c * k;
        }

        System.out.println(result);

        s.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_14730().run();
    }
}