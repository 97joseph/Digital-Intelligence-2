# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# IAE 101 (Fall 2021)
# HW 2, Problem 2

def frequency(c, s):
    # ADD YOUR CODE HERE
    return -1 # CHANGE OR REMOVE THIS LINE
    # 1. First, count the number of times that c appears in s.

    c_occ = 0

    for ch in s:

        if ch==c:

            c_occ += 1

    # 2. Second, compute the total number of characters in s.

    length_s = len(s)

    # 3. Third, divide the result of the step 1 by the result of step 2

    freq = c_occ/length_s

    # 4. Fourth, multiply the result of step 3 by 100.

    freq_perc = freq*100

    # 5. Fifth, round the result to two decimal places

    freq_perc = round(freq_perc, 2)

    # Return the final value as the result of the function

    return freq_perc

result = frequency("i", "Mississippi")

print("The relative frequency is "+str(result)+"%.")

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    s1 = "supercalifragilisticexpialidocious"
    test1 = frequency("a", s1)
    print("s1:", s1)
    print("frequency(\"a\", s1) is:", test1)
    print()

    s2 = "antidisestablishmentarianism"
    test2 = frequency("i", s2)
    print("s2:", s2)
    print("frequency(\"i\", s2) is:", test2)
    print()

    s3 = "mississippi"
    test3 = frequency("i", s3)
    print("s3:", s3)
    print("frequency(\"i\", s3) is:", test3)
    print()

    s4 = "I could have become a mass murderer after I hacked my governor\
module, but then I realized I could access the combined feed of entertainment\
channels carried on the company satellites. It had been well over 35000\
hours or so since then, with still not much murdering, but probably, I\
don't know, a little under 35000 hours of movies, serials, books, plays,\
and music consumed. As a heartless killing machine, I was a terrible failure."
    test4 = frequency("e", s4)
    print("s4:", s4)
    print("frequency(\"e\", s4) is:", test4)
    print()

    s5 = "It was the best of times, it was the worst of times, it was the age of \
wisdom, it was the age of foolishness, it was the epoch of belief, it was the \
epoch of incredulity, it was the season of Light, it was the season of \
Darkness, it was the spring of hope, it was the winter of despair, we had \
everything before us, we had nothing before us, we were all going direct to \
Heaven, we were all going direct the other way – in short, the period was so \
far like the present period, that some of its noisiest authorities insisted \
on its being received, for good or for evil, in the superlative degree of \
comparison only."
    test5 = frequency('t', s5)
    print("s5:", s5)
    print("frequency(\"t\", s5) is:", test5)
    print()
