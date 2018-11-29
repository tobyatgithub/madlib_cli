

WIDTH = 96
ln_one = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} " \
"{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n"

ln_two = "What are a {Large Animal} and backpacking {Small Animal} to do? " \
"Before you can help {A Girl's Name}, you'll have to collect the {Adjective} "\
"{Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} "\
"worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} in"\
"the game, along with hundreds of other goodies for you to find.\n\n"

def extract_key_words(inString):
    """
    This function will take in strings, and return a list with keywords.
    e.g. 
    input: 'I the {Adjective} and {Adjective} {A First Name} have magical power.' (string)
    output: ["Adjective", "Adjective", "A First Name"] (list)
    output2: a template with %s for need-to-fill positions (string)
    """
    # initialize
    store = []
    tmp = ""
    template = ""
    handler = False

    for s in inString:
        # find the trigger { for record
        if s == "{":
            handler = True
            # but we don't want to save { into out output, thus continue
            continue
            
        # find the close trigger } so we stop record, append, and re-init
        if s == "}":
            store.append(tmp)
            handler = False
            tmp = ""
            template += "%s"
            continue

        # record if handler == True
        if handler:
            tmp += s
        else:
            template += s
    
    # we want to return tuple for easier formating
    return store, template

def read_madlib(madlib_file):
    """
    Read a template Madlib file (Example), and parse that file into usable parts.
    input: a path to the madlib file (string)
    output1: a tuple list of needed words (list)
    output2: the paragraph we need to add new works into, the template (string)
    """
    words = []
    para = ""
    with open(madlib_file,'r') as f:
        for line in f:
            # for each line, we extrac word, and create template
            a,b = extract_key_words(line)
            para += b

            # some lines in the template might be empty
            if a != []:
                words += a
    return words, para


def ask_for_word(word_list):
    """
    With the needed word list and template known, this function prompts the user to 
    submit a series of words to fit each of the required components of the Madlib template.
    input: a need-to-input word_list (list of strings), e.g.: ['adj', 'noun']...
    output: a word list that stores user's input (list of strings)
    """
    user_story = []
    for word in word_list:
        print("Give me a %s !\n" %word)
        try:
            user_story.append(input())
        except KeyboardInterrupt:
            print("\nQuit program...")
            exit()

    print("\n\nThanks for the input! .... Gathering creative thoughts!...\n\n")
    return user_story


def format_story(template, user_input):
    """
    With the collected user inputs, populate the template such that each provided input is 
    placed into the correct position within the template.
    input1: a list of words from user's input (list of string)
    input2: a long string of paragraph template got from reading file (string)
    output: a string that put words from input1 into correct locations in input2 (string)
    """
    return (template % tuple(user_input))
    

def print_finished(finished_madlib):
    """
    After the resulting Madlib has been completed, provide the completed response back 
    to the user in the command line.
    input: a finished madlib string (string)
    output: print it 
    """
    print("\n\n...\nHere is the most creative paragraph in this universe!!!\n\n")
    print(finished_madlib)
    print("*" * WIDTH)
    return finished_madlib

def output_finished(content, new_file):
    """
    Write the completed template (Example)to a new file on your file system (in the repo).
    """ 
    with open(new_file, 'w') as f:
        f.write(content)
    # pass

def welcome():
    """
    This is the first called function in our main session that will
    simply print out the welcoming information.
    """

    ln_one = "Welcome to the Madlib Game! "
    ln_two = "Please follow the instruction below."
    ln_three = 'To quit at any time, type "quit"'

    print(" *MAD*" * (WIDTH//6))
    print("*MAD*" + ' ' * (WIDTH-10) + '*MAD*')
    print('*MAD*' + ' ' * ((WIDTH - 10 - len(ln_one))//2) + ln_one + \
    ' ' * ((WIDTH - 10 - len(ln_one))//2) + '*MAD*')
    print("*MAD*" + ' ' * (WIDTH-10) + '*MAD*')
    print('*MAD*' + ' ' * ((WIDTH - 10 - len(ln_two))//2) + ln_two + \
    ' ' * ((WIDTH - 10 - len(ln_two))//2) + '*MAD*')
    print("*MAD*" + ' ' * (WIDTH-10) + '*MAD*')
    print("*MAD*" + ' ' * (WIDTH-10) + '*MAD*')
    print('*MAD*' + ' ' * ((WIDTH - 10 - len(ln_three))//2) + ln_three + \
    ' ' * ((WIDTH - 10 - len(ln_three))//2) + '*MAD*')
    print(" *MAD*" * (WIDTH//6))
    
    print("\n\nMake Me A Video Game!\n")
    print("In this game, you are going to type in several different words...\n")
    print("I will use these words, and magical power, to make it into a telling story!\n")
    print("Here we go!\n\n\n")
    
def run(read_file_path):
    # 1. Print a welcome message to the user, explain
    welcome()

    # 2. Read a template Madlib file (Example), and parse that file into usable parts.
    word_list, template = read_madlib(read_file_path)

    # 3. prompt the user to submit a series of words to fit each of the required components 
    user_input = ask_for_word(word_list)

    # 4. populate the template such that each provided input is placed into the correct position within the template.
    text = format_story(template, user_input)

    # 5. provide the completed response back to the user in the command line.
    save_text = print_finished(text)
    
    # 6. Write the completed template (Example)to a new file on your file system (in the repo).
    output_finished(save_text, './Customized_paragraph.txt')

if __name__ == "__main__":
    run('./example_text.txt')