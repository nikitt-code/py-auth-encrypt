class Init:

    def __init__(self):
        return

    def phone(self, phone: int) -> int:
        try:
            phstr = str(phone)
            step = int(phstr[0])
            for x in range(len(phstr)):
                if not x + 1 == len(phstr):
                    step = (step ** int(phstr[x + 1]) // int(phstr[x + 1]))
            return step % (phone ** 10)
        except:
            return 0

    def password(self, line, step) -> int:
        try:
            line = line.lower()
            hash_sum: int = 1
            for x in range(len(line)):
                curr_let = line[x]
                curr_let_num = ord(curr_let) - 96
                hash_sum *= curr_let_num + ((curr_let_num ** step) % step) ** curr_let_num
            while hash_sum % 10 == 0:
                hash_sum = hash_sum // 10
            return hash_sum
        except:
            return 0
