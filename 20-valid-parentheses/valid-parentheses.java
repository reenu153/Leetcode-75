class Solution {
    public boolean isValid(String s) {
        
        HashMap<Character,Character> bracket_map= new HashMap<>(Map.of(')','(', ']','[','}','{'));
        Stack<Character> stack = new Stack<>();
        Set<Character> open=Set.of('(','{','[');
        for(char c:s.toCharArray()){
            if(open.contains(c)){
                stack.push(c);
                continue;
            }
            if(stack.size()==0 || bracket_map.get(c)!=stack.pop()){
                return false;
            }
        }
        if(stack.size()==0){
            return true;
        }
        return false;
    }
}