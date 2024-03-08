package java_2;

import java.io.*;
import java.util.*;

public class Boj_20301{
    public void run() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()) , k = Integer.parseInt(st.nextToken()) , m = Integer.parseInt(st.nextToken());
        
        // Deque로 가능
        Deque<Integer> d = new ArrayDeque<>();
        for(int i = 1 ; i < n + 1 ; i++)
        {
            d.addLast(i);
        }
        int[] result = new int[n];
        int idx = 0;

        while(d.size() > 1)
        {
            if((int)(idx / m) % 2 == 0)
            {
                for(int i = 0 ; i < k - 1 ; i++)
                {
                    int first = d.removeFirst();
                    d.addLast(first);
                }
                // 저장
                result[idx] = d.removeFirst();
                idx++;
            }
            else
            {
                for(int i = 0 ; i < k - 1 ; i++)
                {
                    int last = d.removeLast();
                    d.addFirst(last);
                }
                // 저장
                result[idx] = d.removeLast();
                idx++;
            }
        }
        result[idx] = d.removeLast();

        for(int num : result)
            System.out.println(num);
    }

    public static void main(String[] args) throws IOException
    {
        new Boj_20301().run();
    }
}