class Solution:
    def intToRoman(self, num: int) -> str:
        coll = [] 
        
        while num >= 1000:
            coll.append("M")
            num -= 1000
        
        if num >= 900:
            coll.append("CM")
            num -= 900
        elif num >= 500:
            coll.append("D")
            num -= 500
        elif num >= 400:
            coll.append("CD")
            num -= 400
        while num >= 100:
            coll.append("C")
            num -= 100
        
        if num >= 90:
            coll.append("XC")
            num -= 90
        elif num >= 50:
            coll.append("L")
            num -= 50
        elif num >= 40:
            coll.append("XL")
            num -= 40
        while num >= 10:
            coll.append("X")
            num -= 10
        
        if num >= 9:
            coll.append("IX")
            num -= 9
        elif num >= 5:
            coll.append("V")
            num -= 5
        elif num >= 4:
            coll.append("IV")
            num -= 4
        while num >= 1:
            coll.append("I")
            num -= 1
        
        return ''.join(coll)