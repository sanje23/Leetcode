class Solution {
    public String sortVowels(String s) {
        
        List<Character>vow= new ArrayList<>();

        for(char i:s.toCharArray()){
            if (i=='a' || i=='e' || i=='o' || i=='u' || i=='i' || i=='A' || i=='E' || i=='I' || i=='O' || i=='U'){
                vow.add(i);
            }
        }
        Collections.sort(vow);
        String res="";
        int k=0;
        for(char i:s.toCharArray()){
            if (i=='a' || i=='e' || i=='o' || i=='u' || i=='i' || i=='A' || i=='E' || i=='I' || i=='O' || i=='U'){
                res+=vow.get(k);
                k++;
            }
            else{
                res+=i;
            }
        }
        return res;
    }
}