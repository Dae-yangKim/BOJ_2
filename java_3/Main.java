package java_3;

import java.io.*;

public class Main{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long minn = 0;

        if(n <= 2)
        {
            minn = (1 * 2) + (1 * 2);
        }
        else
        {
            if(n % 2 == 0)
            {
                long height = (long)(n / 2) - 1;
                minn = (height * 2) + (1 * 2);
            }
            else
            {
                long height = (long)(n / 2);
                minn = (height * 2) + (1 * 2);
            }
        }

        for(int k = 2 ; k <= n; k++)
        {
            long height = (long)(n / (k + 1));
            if(n % (k + 1) == 0)
                height--;
            
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