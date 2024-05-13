class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        losses = defaultdict(int)
        played = set()

        for winner, loser in matches:
            losses[loser] += 1
            played.add(winner)
            played.add(loser)

        no_losses = [player for player in played if losses[player] == 0]
        one_loss = [player for player in played if losses[player] == 1]

        return [sorted(no_losses), sorted(one_loss)]