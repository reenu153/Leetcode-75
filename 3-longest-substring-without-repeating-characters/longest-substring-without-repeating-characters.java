class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len=s.length();
        int l=0;
        Set<Character> seen=new HashSet<>();
        int maxLen=0;
        for (int r=0;r<len;r++){
            while(seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l));
                l+=1;
            }
            seen.add(s.charAt(r));
            maxLen=Math.max(maxLen,r-l+1);
        }
        return maxLen;
    }
}