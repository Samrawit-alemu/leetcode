class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

            n = len(blocks)
            # Count the number of 'W' in the first k blocks
            current_white_count = sum(1 for i in range(k) if blocks[i] == 'W')
            min_recolors = current_white_count

            # Slide the window across the blocks
            for i in range(k, n):
                # Remove the effect of the block that is sliding out
                if blocks[i - k] == 'W':
                    current_white_count -= 1
                # Add the effect of the new block that is sliding in
                if blocks[i] == 'W':
                    current_white_count += 1

                # Update the minimum recolors needed
                min_recolors = min(min_recolors, current_white_count)

            return min_recolors