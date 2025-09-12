class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_cnt = Counter(arr)
        list1 = []
        for i in arr_cnt.values():
            list1.append(i)
        set_list1 = set(list1)
        if len(set_list1) == len(list1):
            return True
        return False
            