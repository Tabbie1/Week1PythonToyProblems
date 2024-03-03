def solution(N):
    # declare the lowercase alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # to repeat twice eg: aabb, the first 15 letters of the alphabet, write this;
    repeated_alphabet = alphabet[:15] * 2
    
    # Truncate the string to length N
    repeated_alphabet = repeated_alphabet[:N]
    
    # use return to present the resulting string
    return repeated_alphabet

# run python3 challenge3.py to confirm the output
print(solution(3))   #it should output'abc'
print(solution(5))   # it should output'abcde'
print(''.join(chr(97 + (i // 2)) for i in range(30)))  #it should output 'aabbccddeeffgghhiijjkkllmmnnoo'
