class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        ArrayList<int[]> merged= new ArrayList<>();
        int i=0;
        int n=intervals.length;
        if(n==0){
            return new int[][]{newInterval};
        }
        while(i<n && intervals[i][1]<newInterval[0]){
            merged.add(intervals[i]);
            i+=1;
        }
        int[] last=newInterval;
        while(i<n && last[1]>=intervals[i][0]){
            last[0]=Math.min(intervals[i][0],last[0]);
            last[1]=Math.max(intervals[i][1],last[1]);
            i+=1;
        }
        merged.add(last);
        while(i<n){
            merged.add(intervals[i]);
            i+=1;
        }

        return merged.toArray(new int[merged.size()][2]);
    }
}