# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/9/23
# Description: The function checks if the first character of subseq matches the first character of seq. If they match,
# the function calls itself recursively with the first character removed from both strings. If they don't match,
# the function calls itself recursively with the first character of seq removed. The function returns True if subseq
# is a subsequence of seq, and False otherwise.

def is_subsequence(subseq, seq):
    """
    Returns True if subseq is a subsequence of seq, and False otherwise.

        subseq: The subsequence to check for.
        seq: The sequence to check in.
    """
    if len(subseq) == 0:
        return True

    if len(seq) == 0:
        return False

    if subseq[0] == seq[0]:
        return is_subsequence(subseq[1:], seq[1:])

    return is_subsequence(subseq, seq[1:])
