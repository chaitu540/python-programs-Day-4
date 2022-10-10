class Solve():
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
   li = ['eat','tea','tan','ate','nat','hat']
  
   print(Solve().Anagrams(li))
