class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int j = 1;
        int profit = 0;
        while (i < prices.size() && j < prices.size()) {
            if (prices[i] > prices[j]) {
                i = j;
            }
            else if (profit < prices[j] - prices[i]) {
                profit = prices[j] - prices[i];
            }
            j++;
        }
        return profit;
    }
};
