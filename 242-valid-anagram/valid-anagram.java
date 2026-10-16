class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> count= new HashMap<>();

        if(s.length()!= t.length()){
            return false;
        }

        for(int i=0;i<s.length();i++){
            count.merge(s.charAt(i),1,Integer::sum);
            count.merge(t.charAt(i),-1,Integer::sum);
        }

        for(char key:count.keySet()){
            if(count.get(key)!=0){
                return false;
            }
        }
        return true;
        
    }
}