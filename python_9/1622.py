while True:
    try:
        a = input()
        b = input()

        a_set = set(a)
        b_set = set(b)

        x = a_set & b_set

        answer = []
        for w in x:
            a_count = a.count(w)
            b_count = b.count(w)
            answer.append(w*min(a_count, b_count))

        answer.sort()
        print(''.join(answer))
    except:
        break