# TASK--------------------------------------------------------------------------------------------
# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# ------------------------------------------------------------------------------------------------
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
# ------------------------------------------------------------------------------------------------
# Concatenate the consecutive strings of strarr by 2, we get:
# ------------------------------------------------------------------------------------------------
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
# ------------------------------------------------------------------------------------------------
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so
# longest_consec(strarr, 2) should return "folingtrashy".
# ------------------------------------------------------------------------------------------------
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# ------------------------------------------------------------------------------------------------
# Note
# consecutive strings : follow one after another without an interruption
# TESTS-------------------------------------------------------------------------------------------
# (["zone", "abigail", "theta", "form", "libe", "zas"], 2) ======================================> "abigailtheta"
# (["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) ===> "oocccffuucccjjjkkkjyyyeehh"
# ([], 3) =======================================================================================> ""
# (["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) =>
# => "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
# (["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) ===================================> "wlwsasphmxxowiaxujylentrklctozmymu"
# (["zone", "abigail", "theta", "form", "libe", "zas"], -2) =====================================> ""
# (["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) ===========================================> "ixoyx3452zzzzzzzzzzzz"
# (["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) ==========================================> ""
# (["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) ===========================================> ""
# CODE--------------------------------------------------------------------------------------------
def longest_consec(strarr=["zone", "abigail", "theta", "form", "libe", "zas"], k=2):
    if k <= 0 or k > len(strarr) or len(strarr) == 0:
        return ''
    result = ''
    quantity = len(strarr) - k + 1
    for x in range(quantity):
        local_str = ''.join(strarr[x: x + k])
        if len(local_str) > len(result):
            result = local_str
    return result


print(longest_consec())
