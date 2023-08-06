//Fibonacci

class Solution {
public:
    int fib(int n) {

        //0, 1, 1, 2, 3, 5, 8, 13

        if (n < 1){
            return 0;
        }

        int previous = 1;
        int prev_prev = 0;
        int result = previous + prev_prev;

        for (size_t i = 2; i <= n; ++i){
            result = previous + prev_prev;

            prev_prev = previous;

            previous = result;
        }

        return result;
    }
};
