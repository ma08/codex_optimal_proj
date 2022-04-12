

def main():
    input_line = input().split()
    n, m, s, d = map(int, input_line)

    input_line = input().split()
    c = list(map(int, input_line))

    #print(n)
    #print(m)
    #print(s)
    #print(d)
    #print(c)

    #Calculate the total number of sodas in the fridge.
    total_sodas = 0
    for i in range(s):
        total_sodas += c[i]

    #print(total_sodas)

    #Calculate the number of sodas needed to fill the fridge.
    sodas_needed = 0
    for i in range(s):
        sodas_needed += d - c[i]

    #print(sodas_needed)

    #If the number of sodas needed is greater than the number of sodas available, then it is impossible to fill the fridge.
    if sodas_needed > n:
        print("impossible")
        return


    #Calculate the number of sodas to put in each slot.
    sodas_in_each_slot = [0 for i in range(s)]

    for i in range(s):
        sodas_in_each_slot[i] = min(d - c[i], n)
        n -= min(d - c[i], n)

    #print(sodas_in_each_slot)

    #Calculate the number of sodas in each slot after the m students have taken sodas.
    sodas_in_each_slot_after_m = [0 for i in range(s)]

    for i in range(s):
        sodas_in_each_slot_after_m[i] = max(c[i] - m, 0)

    #print(sodas_in_each_slot_after_m)

    #Calculate the number of cold sodas that the m students will get
    cold_sodas_m = 0
    for i in range(s):
        cold_sodas_m += sodas_in_each_slot_after_m[i]

    #print(cold_sodas_m)

    #If the number of cold sodas that the m students get is less than m, then it is impossible for all m students to get cold sodas.
    if cold_sodas_m < m:
        print("impossible")
        return


    #Calculate the number of sodas in each slot after the n + m students have taken sodas.
    sodas_in_each_slot_after_n_m = [0 for i in range(s)]

    for i in range(s):
        sodas_in_each_slot_after_n_m[i] = max(c[i] - m + sodas_in_each_slot[i], 0)

    #print(sodas_in_each_slot_after_n_m)

    #Calculate the number of cold sodas that the n + m students will get.
    cold_sodas_n_m = 0
    for i in range(s):
        cold_sodas_n_m += sodas_in_each_slot_after_n_m[i]

    #print(cold_sodas_n_m)

    #Calculate the probability that all m students will get a cold soda.
    prob = cold_sodas_m / total_sodas

    #print(prob)

    #Calculate the probability that all n + m students will get a cold soda.
    prob2 = cold_sodas_n_m / (total_sodas + n)

    #print(prob2)

    #Calculate the probability that all m students will get a cold soda after the new sodas are added.
    prob3 = prob2 / (1 - prob)

    #print(prob3)

    #Print the output.
    for i in range(s):
        print(sodas_in_each_slot[i], end = " ")

if __name__ == "__main__":
    main()
