from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()  # Set to keep track of winners
        losers = Counter()  # Counter to count losses

        for match in matches:
            winner, loser = match
            winners.add(winner)  # Add winner to the winners set
            losers[loser] += 1    # Count losses for the loser

        # Players who never lost
        never_lost = sorted(winners - set(losers.keys()))

        # Players who lost exactly one match
        lost_once = sorted(player for player, count in losers.items() if count == 1)

        return [never_lost, lost_once]

