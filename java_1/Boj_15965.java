package java_1;

import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_15965{
    private ArrayList<Long> arr = new ArrayList<Long>();
    private boolean[] condi;
    private int n = 800000;

    public void eratos()
    {
        condi = new boolean[n + 1];
        // 배열 초기화
        for(int i = 2 ; i < n + 1 ; i++)
            condi[i] = true;

        condi[0] = condi[1] = false;

        // 에라토스테네스의 체
        for(int i = 2 ; i < Math.sqrt(n) + 1 ; i++)
        {
            if(condi[i])
            {
                for(int j = i * i ; j < n + 1 ; j += i)
                {
                    condi[j] = false;
                }
            }
        }
        
    }

    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());

        eratos(); // 에라토스테네스의 체 함수 호출

        for(long i = 2 ; i < n + 1 ; i++)
        {
            if(condi[(int)i])
                arr.add(i);
        }

        System.out.println(arr.get(k - 1));
    }
    
    public static void main(String[] args) throws IOException
    {
        new Boj_15965().run();
    }
}