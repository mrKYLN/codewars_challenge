def anagram_counter(words): 
    if not words:
        return 0
    else:
        sorted_words = []
        for word in words:
            sorted_word = sorted(word)
            convert_string_word = "".join(sorted_word)
            sorted_words.append(convert_string_word)
            
        unique_sorted_words = list(set(sorted_words))
        word_frequence = {}
        for word in unique_sorted_words:
            word_frequence[word] = sorted_words.count(word)
            
        result = 0
        for word, frequence in word_frequence.items():
            calculate_combination = int(frequence*(frequence-1)/2)
            result = result + calculate_combination
        
        return result                
                
# run test function
Test.assert_equals(anagram_counter([]), 0, "Is not returning a number")
Test.assert_equals(anagram_counter(['dell', 'ledl', 'abc', 'cba']), 2)
Test.assert_equals(anagram_counter(['dell', 'ledl', 'lled', 'cba']), 3)
Test.assert_equals(anagram_counter(['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab']), 11)