def main():
    tot_val = 0
    front_val = 0
    end_val = 0
    tmp_val = []
    alph_num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    tmp_word = ""

    # file = open('/Users/Anna Bro/repos/adventOfCode/1/1_input.txt', 'r')
    file = open('/Users/Anna Bro/repos/adventOfCode/1/1_2_test_cases.txt', 'r')
    lines = file.readlines()

    for line in lines:
        for i in line:
            if i.isdigit():
                tmp_val.append(i)
            elif i.isalpha():
                tmp_word = tmp_word + i
                for num_val in alph_num_dict:
                    # TODO: Think of edge cases -- Ex: eightwothree
                    if num_val in tmp_word:
                        tmp_val.append(alph_num_dict[num_val])
                        tmp_word = ""
        front_val = tmp_val[0]
        end_val = tmp_val[len(tmp_val)-1]
        tmp = str(front_val) + str(end_val)
        print("First digit: " + str(front_val) + " | Last digit: " + str(end_val) + " | Two digit: " + str(tmp))
        tot_val += int(tmp)
        tmp_val.clear()
        tmp_word = ""

    print("\nTotal values: " + str(tot_val))

if __name__ == "__main__":
    main()