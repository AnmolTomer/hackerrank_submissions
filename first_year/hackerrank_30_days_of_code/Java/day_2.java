import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";

        Scanner scan = new Scanner(System.in);
                /* Declare second integer, double, and String variables. */
        int j=0; 
        double e=0.0;
        String st;
        j=scan.nextInt();
        e=scan.nextDouble();
        st=scan.nextLine();
        st=scan.nextLine();
        System.out.println(j+i);
        System.out.println(e+d);
        System.out.println(s+st);
        /* Read and save an integer, double, and String to your variables.*/

        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.

        /* Print the sum of both integer variables on a new line. */

        /* Print the sum of the double variables on a new line. */

        /* Concatenate and print the String variables on a new line;
        	the 's' variable above should be printed first. */
         scan.close();
    }
}