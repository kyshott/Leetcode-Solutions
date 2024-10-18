class Solution {
    public void moveZeroes(int[] nums) {
        int pointer = 0;
        int temp = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                temp = nums[pointer];
                nums[pointer] = nums[i];
                nums[i] = temp;
                pointer++;
            }
        }
    }
}

// If nums[i] == 0, then set pointer to i and continue to iterate until i != 0. Then swap, nums[i] with nums[pointer].
// Then, set i back to the pointer value and continue iteration......
