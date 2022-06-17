class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter()

        for c in s:
            cnt[c] += 1

        return next((i for i, c in enumerate(s) if cnt[c] == 1), -1)

    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)

        return next((i for i, c in enumerate(s) if cnt[c] == 1), -1)