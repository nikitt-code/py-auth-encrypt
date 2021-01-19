def str2int(line: str, step: int = 3) -> int:
    line = line.lower()
    lets = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
        "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
        "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
        "x": 24, "y": 25, "z": 26
    }
    hash_sum = 1
    for x in range(len(line)):
        curr_let = line[x]
        hash_sum *= lets[curr_let] + ((lets[curr_let] ** step) % step) ** lets[curr_let]
    while hash_sum % 10 == 0:
        hash_sum = hash_sum // 10
    return hash_sum


def phone2code(phone: int):
    """ beta - with no zeros """
    phstr = str(phone)
    step = int(phstr[0])
    for x in range(len(phstr)):
        if not x + 1 == len(phstr):
            step = (step ** int(phstr[x + 1]) // int(phstr[x + 1]))
    return step % (phone ** 10)


print(str2int("mysupersecreTTTpasswordadwdwa", 5))
# 444157154256036112436072587541693624076755672895177551428225360594572972299194330109409163709150304140202440078016

print(phone2code(77778187276))
# 4319497528477571353237713124486853003085805071461469194183444169461798912207674394836126039668752229278780705
