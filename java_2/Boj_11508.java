package java_2;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Boj_11508{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[n];
        for(int i = 0 ; i < n ; i++)
            arr[i] = Integer.parseInt(br.readLine());
        
        Arrays.sort(arr , Collections.reverseOrder());

        int result = 0;
        int iter = (int)(n / 3);
        for(int i = 0 ; i < iter ; i++)
        {
            Integer[] subArr = Arrays.copyOfRange(arr , i * 3 , i * 3 + 3);
            for(int j = 0 ; j < subArr.length - 1 ; j++)
                result += subArr[j];
        }
        Integer[] subArr = Arrays.copyOfRange(arr , iter * 3 , arr.length);
        for(int i = 0 ; i < subArr.length ; i++)
            result += subArr[i];
        
        System.out.println(result);
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_11508().run();
    }
}