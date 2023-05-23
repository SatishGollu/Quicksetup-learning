
#s ="azABaabza"
#t2 = "TacoCat"
#t3 = "AcZCbaBz"
def Solution(s):
    sub_letters = {}
    count = 0
    for c in s:
        other_letter = c.swapcase()
        if sub_letters.get(other_letter) is None:
            count += 1
            sub_letters[c] = c
        elif sub_letters.get(other_letter) != 0:
            count -= 1
            sub_letters[other_letter] = 0

    if count:
        return -1
    return s

    letters = {}
    for i in range(len(s)):
        c = s[i]
        if letters.get(c.swapcase()) is not None:
            balanced[c] = i
        else:
            letters[c] = i
# get min substring
    min_string = -1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            cur_string = Solution(s[i: j + 1])
            if min_string == -1:
                min_string = cur_string
            else:
                if cur_string != -1:
                    if len(cur_string) < min_string:
                        min_string = cur_string
    return min_string
