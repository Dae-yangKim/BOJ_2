package java_3;

import java.io.*;
import java.util.*;

public class Main{
    public boolean isHol(int n)
    {
        if(n % 2 != 0)
            return true;
        else
            return false;
    }
    
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Integer[] arr = new Integer[n];


        for(int i = 0 ; i < n ; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        
        int result = 0;

        
    }
    
    public static void main(String[] args) throws IOException
    {}
}