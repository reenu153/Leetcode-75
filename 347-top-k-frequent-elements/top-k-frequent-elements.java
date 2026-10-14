class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> count= new HashMap<>();

        for(int num:nums){
            count.merge(num,1,Integer::sum);
        }
        
        PriorityQueue<Integer> heap=new PriorityQueue<>((a,b)->count.get(a)-count.get(b));
        for(int num:count.keySet()){
            heap.offer(num);
            if(heap.size()>k){
                heap.poll();
            }
        }
        int[] res= new int[k];
        for(int i=k-1;i>=0;i--){
            res[i]=heap.poll();
        }

        return res;
    }
}