'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # if length of word is less than the string, return 0
    # base case
    if len(word) < 2:
        return 0

    # if we have a string
    if word[:2] == 'th':
        # found 'th', increment and recursive call until it reaches base case
        return count_th(word[1:]) + 1

    # finished finding and continues on
    return count_th(word[1:])



print(count_th('thhtthht'))
print(count_th('abcthfetwahthth'))