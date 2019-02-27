func repeatedNTimes(A []int) int {
    hashTab := make(map[int]struct{})
    
    for _,number := range A {
        if _,exist := hashTab[number]; exist {
            return number
        } else {
            hashTab[number] = struct{}{}
        }
    }
    
    return A[0]
}
