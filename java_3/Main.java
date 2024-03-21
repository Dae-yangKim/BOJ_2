package java_3;

import java.io.*;
import java.util.*;

public class Main{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long minn = 0;

        if(n % 1 != 0)
        {
            int height = (int)(n / 1) + 1;
            minn = 2 + (height * 2);
        }
        else
        {
            int height = (int)(n / 1);
            minn = 2 + (height * 2);
        }

        for(int k = 2 ; k <= n; k++)
        {
            long height = (long)(n / k);
            if(n % k != 0)
                height++;

            long dul = (k * 2) + (height * 2);
            
            if(dul < minn)
                minn = dul;
        }

        System.out.println(minn);
    }
    
    public static void main(String[] args) throws IOException
    {
        new Main().run();
    }
}