class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_city = [path[0] for path in paths]

        for _ , to_city in paths:
            if to_city not in from_city:
                return to_city
            