class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            cnt, domain = domain.split()
            cnt = int(cnt)

            sub_domain = domain.split('.')
            for i in range(len(sub_domain)):
                ans['.'.join(sub_domain[i:])] += cnt
        return [f"{c} {d}" for d,c in ans.items()]