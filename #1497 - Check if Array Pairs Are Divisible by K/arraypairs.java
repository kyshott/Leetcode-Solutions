class Solution {
    public boolean canArrange(int[] arr, int k) {
        int remainders[] = new int[k];

        for(int i = 0; i < arr.length; i++) {
            int val = arr[i];
            remainders[(val % k + k) % k]++;
        }

        for(int i = 1; i < k; i++) {
            if(remainders[i] < remainders[k - i]) {
                return false;
            }
        }
        
        return remainders[0] % 2 == 0;
    }
}

// (x % k + y % k) % k = 0
// x % k = 3, then y % k = k - 3
// Array to store remainder frequencies.
