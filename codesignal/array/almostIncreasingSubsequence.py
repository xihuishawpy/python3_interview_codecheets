"""
sequence = [1, 3, 2, 1]
almostIncreasingSequence(sequence) = false.

sequence = [1, 3, 2]
almostIncreasingSequence(sequence) = true
"""
def almostIncreasingSequence(sequence):
    
    def isIncreasing(seq):
        return next((i for i in range(len(seq)-1) if seq[i] >= seq[i+1]), -1)
        
    firstTest = isIncreasing(sequence)

    if firstTest == -1:
        return True
    elif isIncreasing(sequence[0:firstTest] + sequence[firstTest+1:]) == -1:
        return True 
    elif isIncreasing(sequence[0:firstTest+1] + sequence[firstTest+2:]) == -1:
        return True 
    
    return False