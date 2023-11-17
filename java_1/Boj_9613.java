package java_1;

import java.util.Scanner;

public class Boj_9613{
    public int gcd(int a , int b)
    {
        if(b == 0) return a;
        return gcd(b , a % b);
    }

    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for(int i = 0 ; i < t ; i++)
        {
            int n = scan.nextInt();
            int[] arr = new int[n];
            for(int j = 0 ; j < arr.length ; j++)
                arr[j] = scan.nextInt();
            
            long result = 0;
            for(int j = 0 ; j < arr.length ; j++)
            {
                for(int k = j + 1 ; k < arr.length ; k++)
                {
                    result += gcd(arr[j] , arr[k]);
                }
            }
            System.out.println(result);
        }
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_9613().run();
    }
}