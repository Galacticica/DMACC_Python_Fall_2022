'''
Program: test_scores.py
Author: Reagan Zierke
Last date modified: 10/19/22

This program takes input of test scores and puts them in a dictionary, then takes the values of the dictionary to average the scores.
'''



def get_test_scores():
    scores_dict=dict()
    number_scores = input("How many test scores? ")
    try:
        number_scores = int(number_scores)
    except:
        pass
    x = 0
    while x < number_scores:
        score_key = f'Score {x+1}'
        score = input(f'Enter score #{x+1}: ')
        try:
            score = int(score)
            if score not in range(0,100):
                raise ValueError()
        except:
            print("Score not in range")
        scores_dict.update({score_key:score})
        x += 1
    return scores_dict

def average_scores(scores):
    length = len(scores)
    keys = scores.keys()
    combined_scores = 0
    for x in keys:
        combined_scores = combined_scores + scores.get(x)
    average_score = combined_scores / length
    print (f'The average of the scores is {average_score: .2f}.')




if __name__ == '__main__':
    scores = get_test_scores()
    average_scores(scores)
