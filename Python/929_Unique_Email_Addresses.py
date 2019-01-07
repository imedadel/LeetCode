class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        for email in emails:
            indexOfAt = email.rfind("@")
            while email.find(".") < indexOfAt:
                email = email.replace(".", "")
            if "+" in email:
                email = "".join(list(email)[email.find("+"),indexOfAt-1])
        
        emails = list(set(emails))
        return len(emails)
