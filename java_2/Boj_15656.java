package java_2;

import java.io.*;
import java.util.*;

public class Boj_15656{
    ArrayList<Integer> al = new ArrayList<>();
    StringBuilder sb = new StringBuilder();

    public void dfs(Integer[] arr , int i , int m)
    {
        if(al.size() == m)
        {
            for(int j = 0 ; j < al.size() ; j++)
            {
                sb.append(al.get(j));
                if(j < al.size() - 1)
                {
                    sb.append(" ");
                }
            }
            sb.append("\n");
            return;
        }

        for(int j = i ; j < arr.length ; j++)
        {
            al.add(arr[j]);
            dfs(arr , 0 , m);
            al.remove(al.size() - 1);
        }
    }

    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Integer[] arr = new Integer[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < arr.length ; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        
        Arrays.sort(arr);

        dfs(arr , 0 , m);
        System.out.println(sb.toString());
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_15656().run();
    }
}