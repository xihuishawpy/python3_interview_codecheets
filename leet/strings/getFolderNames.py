class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        count = collections.Counter()
        seen = set()
        rtn = []

        for root in names:
            k = count[root]
            name = f"{root}({k})" if k else root
            while name in seen:
                k += 1
                name = f"{root}({k})" if k else root

            count[root] = k + 1
            rtn.append(name)
            seen.add(name)

        return rtn
