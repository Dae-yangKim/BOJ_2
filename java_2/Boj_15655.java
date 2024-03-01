package java_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;

public class Boj_15655{
    ArrayList <Integer> al = new ArrayList<>();
    StringBuilder sb = new StringBuilder();

    public void dfs(Integer[] arr , int i , int M)
    {
        if(al.size() == M)
        {
            for(int k = 0 ; k < al.size() ; k++)
            {
                sb.append(al.get(k));
                if(k < al.size() - 1)
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
            dfs(arr , j + 1 , M);
            al.remove(al.size() - 1);
        }
    }

    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()) , M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Integer[] arr = new Integer[N];

        for(int i = 0 ; i < N ; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        
        Arrays.sort(arr);

        dfs(arr , 0 , M);
        System.out.println(sb.toString());
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_15655().run();
    }
}