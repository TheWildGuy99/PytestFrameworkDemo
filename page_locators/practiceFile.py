class SandClock:

    def create_sandclock_pattern(self):
        sand_size = int(input("Enter the size:"))

        if sand_size%2 !=0:
            sand_size = sand_size+1

        sub_size = int(sand_size/2)
        first_pyramid = "*"
        leading_space = "_"
        temp_line = ""
        for i in range(1,sub_size):
            for j in range(sub_size-1):
                leading_space = leading_space + "_"
            for j in range(2*i + 1):
                temp_line = first_pyramid + "*"
            print(leading_space + temp_line + leading_space)
            sub_size = sub_size-1
            leading_space = "_"

