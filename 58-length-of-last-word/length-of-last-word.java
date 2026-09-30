class Solution {
    public int lengthOfLastWord(String s) {
        String[] str = s.trim().split("\\s+");
        int n = str.length - 1 ;
        return str[n].length();
    }
}