func numJewelsInStones(J string, S string) int {
    sum := 0
    
    for _, stone := range S {
        for _, jewel := range J {
            if stone == jewel {
                sum++
            }
        }
    }
    return sum
}
