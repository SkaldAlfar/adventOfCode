def main():
    tot_val = 0
    front_val = 0
    end_val = 0
    tmp_val = []

    file = open('/Users/Anna Bro/repos/adventOfCode/1/1_input.txt', 'r')
    lines = file.readlines()

    for line in lines:
        for i in line:
            if i.isdigit():
                tmp_val.append(i)
        front_val = tmp_val[0]
        end_val = tmp_val[len(tmp_val)-1]
        tmp = str(front_val) + str(end_val)
        print("First digit: " + str(front_val) + " | Last digit: " + str(end_val) + " | Two digit: " + str(tmp))
        tot_val += int(tmp)
        tmp_val.clear()

    print("\nTotal values: " + str(tot_val))

if __name__ == "__main__":
    main()