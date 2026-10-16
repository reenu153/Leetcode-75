class Solution {
    public int countSubstrings(String s) {
        char[] str= s.toCharArray();
        int n=str.length;
        int count=0;
        for(int i=0;i<n;i++){
            int l=i;
            int r=i;
            while(l>=0 && r<n && str[l]==str[r]){
                count+=1;
                l--;
                r++;
            }
            l=i;
            r=i+1;
            while(l>=0 && r<n && str[l]==str[r]){
                count+=1;
                l--;
                r++;
            }
        }
        return count;
    }
}