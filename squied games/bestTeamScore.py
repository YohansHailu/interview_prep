class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age = []; score = []
        for a,s in sorted(zip(ages, scores)):
            age.append(a)
            score.append(s)
        
        n = len(age)
        dp = score.copy()

        for i in range(len(dp)):
            for j in range(i):
                if score[i] >= score[j]:
                    dp[i] = max(dp[i], dp[j] + score[i])
        
        return max(max(dp), max(score))
