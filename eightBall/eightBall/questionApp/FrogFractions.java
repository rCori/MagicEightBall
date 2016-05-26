// you can also use imports, for example:
import java.util.Arrays;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int[] A) {
        // write your code in Java SE 8
        int[] leafCount = new int[X];
        Arrays.fill(leafCount, -1);
        for(int i  = 0; i < A.length; i++) {
            //Store the index i at leafCount[A[i]]
            //First check if it has not been used yet, we only want the first occurance
            if(leafCount[A[i]-1] == -1) {
                leafCount[A[i]-1] = i;
            }
        }
        int maxIndex = -1;
        for(int j : leafCount) {
            //This portion of array A never covers this space
            if(j == -1){
                return -1;
            }
            if(j > maxIndex) {
                maxIndex = j;
            }
        }
        return maxIndex;
    }
}