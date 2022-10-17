def is_year_leap(year):
    if year // 4:
        return True
    else:
        return False

def main():
    test_data = [1990,2000,2016,1987]
    test_results = [False,True,True,False]

    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr,"->",end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
main()
