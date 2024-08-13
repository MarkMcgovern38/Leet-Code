class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1){
            return x;
        }

        int start = 1;
        int end = x;
        int result = 0;

        while (start <= end) {
            int mid = (end + start) / 2;
        
            if (mid <= x / mid) {
                result = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;

    }
}
