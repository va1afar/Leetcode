class Solution {
 public int minPartitions(String n) {
        int max=-1;
        for(int i=0;i!=n.length();++i)
        {
            if(n.codePointAt(i)-'0'>max)
            {
                max=n.codePointAt(i)-'0';
            }
        }
        return max;
    }
}