class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int res=0;
        vector<int>seen;
        for(int f:fruits){
            int flag=0;
            for(int i=0;i<baskets.size();i++){
                if((f<=baskets[i])&&(find(seen.begin(),seen.end(),i)==seen.end())){
                    seen.push_back(i);
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                res++;
            }
        }
        return res;
        
    }
};