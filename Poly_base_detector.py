import matplotlib
import numpy
from matplotlib import pyplot as plt

# The goal of the script is to count the instances of repeating bases of "T" and "A"s in a DNA sequence
# It should log the length and distribution of the "poly-T" or "poly-A"

# Create a sliding window with a counter

def Poly_base_detector():
    sequence = input("Enter Your Sequence version4")
    t_counter = 0
    a_counter =0
    t_bank = []
    a_bank = []
    max_length = (len(sequence)-1)
    for i in range(len(sequence)):
        test_base = sequence[i]
        if test_base == "T" or test_base == "t":
            t_counter += 1
            a_bank.append(a_counter)
            a_counter = 0
            if i == max_length:
                t_bank.append(t_counter)
            else:
                t_counter = t_counter
        elif test_base == "A" or test_base == "a":
            a_counter += 1
            t_bank.append(t_counter)
            t_counter = 0
            if i == max_length:
                a_bank.append(a_counter)
            else:
                a_counter = a_counter
        else:
            t_bank.append(t_counter)
            a_bank.append(a_counter)
            t_counter = 0
            a_counter = 0

    # Compress the data and filter out 0, 1, 2, 3 values
    sorted_t_bank = []
    sorted_a_bank = []
    for j in range(len(t_bank)):
        t_bank_cycler = t_bank[j]
        if t_bank_cycler >= 4:
            sorted_t_bank.append(t_bank_cycler)
    print(sorted_t_bank)

    for k in range(len(a_bank)):
        a_bank_cycler = a_bank[k]
        if a_bank_cycler >= 4:
            sorted_a_bank.append(a_bank_cycler)
    print(sorted_a_bank)

    # Plot

    bins = numpy.linspace(0, 10, 10)
    plt.hist(sorted_a_bank, bins, alpha=0.5, label='Poly A')
    plt.hist(sorted_t_bank, bins, alpha=0.5, label='Poly T')
    plt.legend(loc='upper right')
    plt.title('Slide27')
    plt.xlabel('Length of Poly-base')
    plt.ylabel('Frequency')
    plt.show()
    #plt.savefig('Input'+str(i)+'.png')

Poly_base_detector()
