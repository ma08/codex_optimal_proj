

import sys


def main():
    n, m = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(m)]

    # convert the input to a list of lists that contains the gates allowed by each ID card
    allowed_gates = [[] for _ in range(n)]
    for i in range(m):
        for j in range(gates[i][0] - 1, gates[i][1]):
            allowed_gates[j].append(i)

    # initialize the number of ID cards which allow to pass all the gates alone
    num_cards = 0

    # iterate through the list of lists of allowed gates for each ID card
    for allowed in allowed_gates:
        # find the number of gates which are allowed by only this ID card
        # by finding the difference between the number of allowed gates and the number of gates allowed by all the other ID cards
        num_alone = len(allowed) - len(set(allowed) - set(allowed_gates[0]) - set(allowed_gates[1]) - set(allowed_gates[2]) - set(allowed_gates[3]) - set(allowed_gates[4]) - set(allowed_gates[5]) - set(allowed_gates[6]) - set(allowed_gates[7]) - set(allowed_gates[8]) - set(allowed_gates[9]) - set(allowed_gates[10]) - set(allowed_gates[11]) - set(allowed_gates[12]) - set(allowed_gates[13]) - set(allowed_gates[14]) - set(allowed_gates[15]) - set(allowed_gates[16]) - set(allowed_gates[17]) - set(allowed_gates[18]) - set(allowed_gates[19]) - set(allowed_gates[20]) - set(allowed_gates[21]) - set(allowed_gates[22]) - set(allowed_gates[23]) - set(allowed_gates[24]) - set(allowed_gates[25]) - set(allowed_gates[26]) - set(allowed_gates[27]) - set(allowed_gates[28]) - set(allowed_gates[29]) - set(allowed_gates[30]) - set(allowed_gates[31]) - set(allowed_gates[32]) - set(allowed_gates[33]) - set(allowed_gates[34]) - set(allowed_gates[35]) - set(allowed_gates[36]) - set(allowed_gates[37]) - set(allowed_gates[38]) - set(allowed_gates[39]) - set(allowed_gates[40]) - set(allowed_gates[41]) - set(allowed_gates[42]) - set(allowed_gates[43]) - set(allowed_gates[44]) - set(allowed_gates[45]) - set(allowed_gates[46]) - set(allowed_gates[47]) - set(allowed_gates[48]) - set(allowed_gates[49]) - set(allowed_gates[50]) - set(allowed_gates[51]) - set(allowed_gates[52]) - set(allowed_gates[53]) - set(allowed_gates[54]) - set(allowed_gates[55]) - set(allowed_gates[56]) - set(allowed_gates[57]) - set(allowed_gates[58]) - set(allowed_gates[59]) - set(allowed_gates[60]) - set(allowed_gates[61]) - set(allowed_gates[62]) - set(allowed_gates[63]) - set(allowed_gates[64]) - set(allowed_gates[65]) - set(allowed_gates[66]) - set(allowed_gates[67]) - set(allowed_gates[68]) - set(allowed_gates[69]) - set(allowed_gates[70]) - set(allowed_gates[71]) - set(allowed_gates[72]) - set(allowed_gates[73]) - set(allowed_gates[74]) - set(allowed_gates[75]) - set(allowed_gates[76]) - set(allowed_gates[77]) - set(allowed_gates[78]) - set(allowed_gates[79]) - set(allowed_gates[80]) - set(allowed_gates[81]) - set(allowed_gates[82]) - set(allowed_gates[83]) - set(allowed_gates[84]) - set(allowed_gates[85]) - set(allowed_gates[86]) - set(allowed_gates[87]) - set(allowed_gates[88]) - set(allowed_gates[89]) - set(allowed_gates[90]) - set(allowed_gates[91]) - set(allowed_gates[92]) - set(allowed_gates[93]) - set(allowed_gates[94]) - set(allowed_gates[95]) - set(allowed_gates[96]) - set(allowed_gates[97]) - set(allowed_gates[98]) - set(allowed_gates[99]) - set(allowed_gates[100]) - set(allowed_gates[101]) - set(allowed_gates[102]) - set(allowed_gates[103]) - set(allowed_gates[104]) - set(allowed_gates[105]) - set(allowed_gates[106]) - set(allowed_gates[107]) - set(allowed_gates[108]) - set(allowed_gates[109]) - set(allowed_gates[110]) - set(allowed_gates[111]) - set(allowed_gates[112]) - set(allowed_gates[113]) - set(allowed_gates[114]) - set(allowed_gates[115]) - set(allowed_gates[116]) - set(allowed_gates[117]) - set(allowed_gates[118]) - set(allowed_gates[119]) - set(allowed_gates[120]) - set(allowed_gates[121]) - set(allowed_gates[122]) - set(allowed_gates[123]) - set(allowed_gates[124]) - set(allowed_gates[125]) - set(allowed_gates[126]) - set(allowed_gates[127]) - set(allowed_gates[128]) - set(allowed_gates[129]) - set(allowed_gates[130]) - set(allowed_gates[131]) - set(allowed_gates[132]) - set(allowed_gates[133]) - set(allowed_gates[134]) - set(allowed_gates[135]) - set(allowed_gates[136]) - set(allowed_gates[137]) - set(allowed_gates[138]) - set(allowed_gates[139]) - set(allowed_gates[140]) - set(allowed_gates[141]) - set(allowed_gates[142]) - set(allowed_gates[143]) - set(allowed_gates[144]) - set(allowed_gates[145]) - set(allowed_gates[146]) - set(allowed_gates[147]) - set(allowed_gates[148]) - set(allowed_gates[149]) - set(allowed_gates[150]) - set(allowed_gates[151]) - set(allowed_gates[152]) - set(allowed_gates[153]) - set(allowed_gates[154]) - set(allowed_gates[155]) - set(allowed_gates[156]) - set(allowed_gates[157]) - set(allowed_gates[158]) - set(allowed_gates[159]) - set(allowed_gates[160]) - set(allowed_gates[161]) - set(allowed_gates[162]) - set(allowed_gates[163]) - set(allowed_gates[164]) - set(allowed_gates[165]) - set(allowed_gates[166]) - set(allowed_gates[167]) - set(allowed_gates[168]) - set(allowed_gates[169]) - set(allowed_gates[170]) - set(allowed_gates[171]) - set(allowed_gates[172]) - set(allowed_gates[173]) - set(allowed_gates[174]) - set(allowed_gates[175]) - set(allowed_gates[176]) - set(allowed_gates[177]) - set(allowed_gates[178]) - set(allowed_gates[179]) - set(allowed_gates[180]) - set(allowed_gates[181]) - set(allowed_gates[182]) - set(allowed_gates[183]) - set(allowed_gates[184]) - set(allowed_gates[185]) - set(allowed_gates[186]) - set(allowed_gates[187]) - set(allowed_gates[188]) - set(allowed_gates[189]) - set(allowed_gates[190]) - set(allowed_gates[191]) - set(allowed_gates[192]) - set(allowed_gates[193]) - set(allowed_gates[194]) - set(allowed_gates[195]) - set
        # if the number of gates alone is equal to the total number of gates, then this ID card allows to pass all the gates alone
        if num_alone == m:
            num_cards += 1

    print(num_cards)


if __name__ == '__main__':
    main()
