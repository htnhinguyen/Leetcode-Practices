class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j = 1, m = 1;
        while (j < nums.size()){
            if (nums[i] == nums[j] && m < 2) {
                i++;
                swap(nums[i],nums[j]);
                m++;
            }
            else if (nums[i] != nums[j] && m >= 2) {
                i++;
                swap(nums[i],nums[j]);
                m = 1;
            }
            else if (nums[i] != nums[j] && m < 2) {
                i++;
                swap(nums[i],nums[j]);
            }
            j++;
        }
        if (m == 2 && nums[i] < nums[j-1]) {
            swap(nums[i],nums[j-1]);
        }       
        return i+1;
    }
};
