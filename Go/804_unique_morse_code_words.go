func uniqueMorseRepresentations(words []string) int {
    uniq := make(map[string]struct{})
    MORSE := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    
    for _, word := range words {
        morseWord := ""
        for _, c := range word {
            morseWord += MORSE[c - 'a']
        }
        
        if _, present := uniq[morseWord]; !present {
            uniq[morseWord] = struct{}{}
        }
    }
    return len(uniq)
}
