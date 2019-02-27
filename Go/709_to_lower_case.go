func toLowerCase(str string) string {
    r := []rune(str)
    
    for i := range r {
        if r[i] >= 65 && r[i] <= 90 {
            r[i] += 32
        }
    }
    
    return string(r)
}
