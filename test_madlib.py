from madlib import run, extract_key_words, format_story


ln_one = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} " \
"{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n"

ln_two = "What are a {Large Animal} and backpacking {Small Animal} to do? " \
"Before you can help {A Girl's Name}, you'll have to collect the {Adjective} "\
"{Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} "\
"worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} in"\
"the game, along with hundreds of other goodies for you to find.\n\n"


def test_run_exist():
    assert(run)

def test_extract_key_words():
    ln_one = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} " \
    "{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n"

    actual = extract_key_words(ln_one)    
    expected1 = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun']
    # notice that copy paste string from other source may cause error
    expected2 = "I the %s and %s %s have %s %s's %s sister and plan to steal her %s %s!\n"
    assert(expected1 == actual[0])
    assert(expected2 == actual[1])


def test_format_story1():
    assert(format_story("111 %s %s %s", ["a","b","c"])=="111 a b c")