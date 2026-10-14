class Solution {
    public boolean exist(char[][] board, String word) {
        char[] w = word.toCharArray();
        for (int i=0; i < board.length; i++)
            for (int j=0; j < board[0].length; j++) {
                if (search(board, i, j, w, 0)){
                    return true;
                }
            }
        return false;

    }

    private boolean search(char[][] board,int r, int c, char[] word, int idx){
        if(idx==word.length){
            return true;
        }

        if( r>=board.length||c>=board[0].length||r<0||c<0||board[r][c]!=word[idx]||board[r][c]=='#'){
            return false;
        }


        char ch=board[r][c];
        board[r][c]='#';

        if (
            search(board,r+1,c,word,idx+1)||search(board,r-1,c,word,idx+1)||search(board,r,c+1,word,idx+1)||search(board,r,c-1,word,idx+1)
        ){
            return true;
        }
        
        board[r][c]=ch;
        return false;
    }
}