lass Solve():
   def Anagrams( self, li ):
       
       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))
           
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]
          
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

if __name__ == '__main__':
   li = ['pop','bat','tab','opp']
  
   print(Solve().Anagrams(li))
