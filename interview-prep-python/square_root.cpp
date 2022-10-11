/* 
File: square_root

Author: DaviZCodes

Question:

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
*/

//the best approach is through sorting and using a while loop with mid point 

class Solution {
public: 
  int mySqrt(int x) {
    long long int p = 1, q = x;
    while (p <= q) {
      long long int mid_point = p + (q - p)/2;
      
      //if value is found, return it
      if (mid_point * mid_point == x){
        return mid_point;
      }
      
      //square roots tend to be smaller numbers, we want to first eliminate on the greater half by decreasing q
      else if (mid_point * mid_point > x){
        q = mid_point - 1;
      }
      
      else{
        p = mid_point + 1;
      }
    }
    return q;
  }
};


/* This is my first attempt on the solution. I just saw if i*i is smaller or equal to the target value, and (i+1)*(i+1) is bigger than the target
value and this would return i. But this would have a large runtime

class Solution {
public:
    int mySqrt(int x) {
        for (long i = 0; i <= x; i++) {
            if (i*i <= x && (i+1)*(i+1) > x) {
                return floor(i);
            }
        }
        return 0;
    }
};

*/
