package java_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_1940{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n ; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        
        int result = 0;
        for(int s = 0 ; s < n ; s++)
        {
            int summ = 0;
            int e = s + 1;

            while(e < n)
            {
                summ = arr[s];
                summ += arr[e++];
                if(summ == m)
                {
                    result++;
                    break;
                }
            }
        }

        System.out.println(result);
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_1940().run();
    }
}