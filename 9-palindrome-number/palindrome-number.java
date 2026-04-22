class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0,rem;
        int temp=0;
          temp = x;
          while(x>0){
            rem = x%10;
            rev= (rev*10)+rem;
            x = x/10;

          }
          return (rev==temp);
           
          
    }
}