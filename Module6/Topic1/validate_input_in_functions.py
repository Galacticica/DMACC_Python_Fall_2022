'''
Program: validate_input_in_functions.py
Author: Reagan Zierke
Last date modified: 10/03/22

This program validates the test scores and returns the score or an invalid statement.
'''




def score_input(test_name, test_score=-1, invalid_input='Invalid test score!'):
    '''
    This function validates that a test score is within the specific range
    :param test_name: Name of the test
    :param test_score: Test score
    :param invalid_input: Message outputed if test score is invalid
    '''
    try:
        test_score = int(test_score)
        if test_score in range(1,100):
            return (f"{test_name}: {test_score}")
        return (f"{test_name}: {invalid_input}")
    except:
        return (f"{test_name}: {invalid_input}")









if __name__ == '__main__':
    #Accurate Input
    display_string = score_input("Test 1", 98)
    print(display_string)
    #Input too low
    display_string = score_input("Test 2", -12)
    print(display_string)
    #Input too high
    display_string = score_input("Test 3", 103)
    print(display_string)
    #Invalid input
    display_string = score_input("Test 4", "potato", "ValueError Encountered")
    print(display_string)

