package java_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj_9471 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringBuilder builder = new StringBuilder();
        
        for(int i = 0; i<n; i++) {
            String[] tmp = reader.readLine().split(" ");
            int m = Integer.parseInt(tmp[1]);
            
            int a = 1;
            int b = 1;
            int count = 0;
            
            while(true) {
                int next = (a + b) % m;
                a = b;
                b = next;
                count ++;
                
                if (a == 1 && b == 1) {
                    break;
                }
            }
            
            builder.append(i + 1).append(" ").append(count).append("\n");
        }
    
        System.out.println(builder);
    }
}