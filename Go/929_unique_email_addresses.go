func numUniqueEmails(emails []string) int {
    
    filteredEmails := make(map[string]struct{})
    
    for _, email := range emails {
        s := strings.Split(email, "@")
        local, domain := s[0], s[1]
        localSplit := strings.Split(local, "+")
        local = localSplit[0]
        
        local = strings.Replace(local, ".", "", -1)
        
        if _, present := filteredEmails[local + "@" + domain]; !present {
            filteredEmails[local + "@" + domain] = struct{}{}
        }
    }
    return len(filteredEmails)
}
