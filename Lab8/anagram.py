def check_anagram_using_recursion(word1, word2):
    """
    Checks if two words are anagrams of each other.
    :param word1:
    :param word2:
    :return:
    """
    if len(word1) != len(word2):
        return False
    if len(word1) == 0:
        return True
    if word1[0] != word2[0]:
        return False
    return check_anagram_using_recursion(word1[1:], word2[1:])


print(check_anagram_using_recursion("abc", "cab"))