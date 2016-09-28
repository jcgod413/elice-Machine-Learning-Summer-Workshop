import re
import math

def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)

    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print(calculate_doc_prob(training_model, testing_model, alpha))

def calculate_doc_prob(training_model, testing_model, alpha):
    logprob = 0

    for b in testing_model:
        dup = testing_model[b]
        den = sum(training_model.values()) + (len(training_model) * alpha)

        try: logprob += math.log((training_model[b] + alpha) / den) * dup
        except: logprob += math.log(alpha / den) * dup

    return logprob

def create_BOW(sentence):
    bow = {}

    lower_bow = sentence.lower()
    modified_bow = replace_non_alphabetic_chars_to_space(lower_bow)
    bowList = modified_bow.split()

    for b in bowList:
        if len(b) < 1:
            bowList.remove(b)
        else:
            if b in bow :
                bow[b] = bow[b] + 1
            else:
                bow[b] = 1

    return bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()
