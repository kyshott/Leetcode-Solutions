class Solution {
    public int[] applyOperations(int[] nums) {

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                nums[i - 1] = 2 * nums[i - 1];
                nums[i] = 0;
            }
        }

        int pointer = 0;
        int temp = 0;

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != 0) {
                temp = nums[pointer];
                nums[pointer] = nums[j];
                nums[j] = temp;
                pointer++;
            }
        }

        return nums;
    }
}
