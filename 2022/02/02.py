import os

if __name__ == '__main__':
    values = open('/config/workspace/AoC/2022/02/input.txt').readlines()
    score = 0
    d1 = {'A': 1, 'B': 2, 'C': 3}

    for v in values:
        opp, me = v.split(' ')

        # match me.strip():
        #     case 'X':
        #         me = 'A'
        #     case 'Y':
        #         me = 'B'
        #     case 'Z':
        #         me = 'C'

        match me.strip():
            case 'X':
                if opp == 'A':
                    me = 'C'
                elif opp == 'B':
                    me = 'A'
                else:
                    me = 'B'
            case 'Y':
                me = opp
            case 'Z':
                if opp == 'A':
                    me = 'B'
                elif opp == 'B':
                    me = 'C'
                else:
                    me = 'A'

        if opp == me:
            score += 3

        if opp == 'A' and me == 'B':

            score += 6

        if opp == 'A' and me == 'C':
            print('loss')

        if opp == 'B' and me == 'C':
            print('win')
            score += 6

        if opp == 'B' and me == 'A':
            print('loss')

        if opp == 'C' and me == 'A':
            score += 6

        if opp == 'C' and me == 'B':
            print('loss')
            
        score += d1[me]    
    print(score)