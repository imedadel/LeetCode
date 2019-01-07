class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        cleanEmails = set()
        
        for email in emails:
            local, domain = email.split("@")
            
            if "+" in local:
                local = local[:local.index("+")]
            local = local.replace(".","")
            cleanEmails.add(local + "@" + domain)
        
        return len(cleanEmails)
