class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {

        Set<Character>set = new HashSet<>();
        for(char c: brokenLetters.toCharArray()){
            set.add(c);
        }
        int c=0;
        String[] l = text.split(" ");
        for(String i:l){
            for(char ch:i.toCharArray()){
                if(set.contains(ch)){
                    c++;
                    break;
                }
            }
        }
        return l.length-c;
        
    }   
}