import re

def main():
    sentence = input()
    BOW = create_BOW(sentence)

    print(BOW)

def create_BOW(sentence):
    bow = {}

    # Exercise
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
