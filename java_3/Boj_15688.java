package java_3;

import java.util.*;
import java.io.*;

public class Boj_15688{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        Integer[] arr = new Integer[n];
        for(int i = 0 ; i < n ; i++)
            arr[i] = Integer.parseInt(br.readLine());
        
        Arrays.sort(arr);

        for(int i = 0 ; i < n ; i++)
            sb.append(arr[i]).append("\n");
        
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException
    {
        new Boj_15688().run();
    }
}