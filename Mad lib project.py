# Mad lib project
# prompter uses a .txt file of word types to prompt the user for later population in the madlib
# creator turns the user input along with a template .txt file into the finished madlib

def prompter(file):
    # prompt_complete is a list we will be adding to and returning with the user input
    prompt_complete = []
    # We open our file and create a list of all of the word types based on it
    prompt = open(file).read()
    p_list = prompt.split(',')
    # this loop asks the user for their inputs and appends them to prompt_complete
    for i in p_list:
        ans = input('Please give me ' + i + ': ')
        prompt_complete.append(ans)
    return prompt_complete

def creator(file, ins_list):
    # The template file has 'insert' in every blank field of the mad lib
    # we split the template text on 'insert so we can put the user's inputs where they need to go
    full_lib = open(file).read()
    spl = full_lib.split('insert')
    penult = [] # penult is the list we will append to to make the complete product
    # this loop appends to penult in such a way that we get the inputs in the right spots
    for i in range(0, len(ins_list)):
        penult.append(spl[i])
        penult.append(ins_list[i])
    penult.append(spl[-1]) # we need to have the last of the template here because of how the mad lib is structured
    final = '' # we will add to this string with a loop through penult
    for i in penult:
        final += i
    print(final)


def main():
    print('This is a Mad Lib Game!\nPlease give me a couple words that I\'ll ask for and then I\'ll tell you a story\n')
    p = 'C:/Users/Daniel/OneDrive/Documents/Python Scripts/madlib_prompt.txt'
    t = 'C:/Users/Daniel/OneDrive/Documents/Python Scripts/madlib_template.txt'
    ins_list = prompter(p)
    print('\nHere is the story!\n')
    creator(t, ins_list)

main()