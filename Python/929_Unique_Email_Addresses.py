class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = set()
        for email in emails:
            local,domain = email.split('@')
            if '+' in local: local = local[:local.index('+')]
            local = local.replace('.', '')
            ans.add(local+'@'+domain)
        return len(ans)
