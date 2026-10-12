class Solution {
    public int firstIndex(int[] nums, int target){
        int l=0;
        int r=nums.length-1;
        int index=-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(nums[mid]==target){
                index=mid;
                r=mid-1;
            }
            else if(nums[mid]>target){
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return index;
    }
       public int lastIndex(int[] nums, int target){
        int l=0;
        int r=nums.length-1;
        int index=-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(nums[mid]==target){
                l=mid+1;
                index=mid;
            }
            else if(nums[mid]>target){
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return index;
    }
    public int[] searchRange(int[] nums, int target) {
        int[] arr={-1,-1};
        arr[0] = firstIndex(nums,target);
        arr[1]=lastIndex(nums,target);
        return arr;
    }
}