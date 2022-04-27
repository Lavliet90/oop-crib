# print([2 ** x for x in range(1, 11)])
#
# ls = [1 << i for i in range(1, 10)]
# print(ls)


def pig_it(text):
    full = []
    for word in text.split(' '):
        if word.isalpha():
            right_list = []
            right_list.append([word[letter] for letter in range(1, len(word))])
            right_list[0].append(word[0])
            right_list[0].append('ay')
            right_str = "".join(right_list[0])
            full.append(right_str)
        else:
            full.append('!')
    print(" ".join(full))
    return " ".join(full)

pig_it('Pig latin is cool')  # igPay atinlay siay oolcay
pig_it('Hello world !')