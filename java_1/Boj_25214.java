package java_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_25214{
    private int n , ans , minIndex;
    int[] arr;
    
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        StringBuilder sb = new StringBuilder();
        ans = minIndex = 0;

        for(int i = 0 ; i < n ; i++)
        {
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] < arr[minIndex]) minIndex = i;
            if(arr[i] - arr[minIndex] > ans)
            {
                ans = arr[i] - arr[minIndex];
            }
            sb.append(ans).append(' ');
        }
        System.out.println(sb);
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_25214().run();
    }
}