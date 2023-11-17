package java_1;

import java.util.Scanner;

public class Boj_5347{
    public long gcd(int a , int b)
    {
        if(b == 0) return a;
        else return gcd(b , a % b);
    }
    
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for(int i = 0 ; i < n ; i++)
        {
            int a = scan.nextInt();
            int b = scan.nextInt();

            long result;
            if(a > b)
                result = gcd(a , b);
            else
                result = gcd(b , a);
            
            System.out.println((a * b) / result);
        }
        
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_5347().run();
    }
}