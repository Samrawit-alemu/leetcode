class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #can do cows - bulls 
        sorted_secret = "".join(sorted(secret))
        sorted_guess = "".join(sorted(guess))
        cows = 0 
        sP =0
        gP = 0
        while (sP<len(sorted_secret) and gP<len(sorted_guess)):
            if (sorted_secret[sP]==sorted_guess[gP]):
                sP+=1
                gP+=1
                cows+=1
            elif (sorted_secret[sP]>sorted_guess[gP]):
                gP+=1
            else:
                sP+=1
        bulls=0
        sP =0
        gP = 0
        while (sP<len(secret) and gP<len(guess)):
            if (secret[sP]==guess[gP]):
                bulls+=1
            sP+=1
            gP+=1
        cows = cows-bulls
        return (""+str(bulls)+"A"+str(cows)+"B")
            
            

        