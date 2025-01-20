class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> hmap = {};
        for (int i = 0; i < nums.size(); i++) {
            hmap[nums[i]] += 1;
            if (hmap[nums[i]] > int(nums.size()/2)) {
                return nums[i];
            }
        }  
        return -1;        
    }
};
