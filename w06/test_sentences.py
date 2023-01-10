from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(20):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(20):
        noun = get_noun(5)
        assert noun in plural_nouns


def test_get_verb():
    verbs = ["drank", "ate", "grew", "laughed", "thought",
             "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(20):
        verb = get_verb(1, "past")
        assert verb in verbs

    verbs = ["drink", "eat", "grow", "laugh", "think",
             "run", "sleep", "talk", "walk", "write"]
    for _ in range(20):
        verb = get_verb(8, "present")
        assert verb in verbs

    verbs = ["will drink", "will eat", "will grow", "will laugh",
             "will think", "will run", "will sleep", "will talk",
             "will walk", "will write"]
    for _ in range(20):
        verb = get_verb(3, "future")
        assert verb in verbs


def test_get_preposition():
    assert get_preposition() in ["about", "above", "across", "after", "along",
                                 "around", "at", "before", "behind", "below",
                                 "beyond", "by", "despite", "except", "for",
                                 "from", "in", "into", "near", "of",
                                 "off", "on", "onto", "out", "over",
                                 "past", "to", "under", "with", "without"]


def test_get_prepositional_phrase():
    assert len(get_prepositional_phrase(1).split(' ')) == 3
    assert len(get_prepositional_phrase(2).split(' ')) == 3


def test_get_adjective():
    assert get_adjective() in ["adorable", "adventurous", "aggressive", "agreeable", "alert", "alive",
                               "amused", "angry", "annoyed", "annoying", "anxious", "arrogant", "ashamed", "attractive", "average"]


def test_get_adverb():
    assert get_adverb() in ["accidentally", "closely", "eventually", "fortunately",
                            "irritably", "mortally", "painfully", "powerfully", "roughly", "softly"]

    # Call the main function that is part of pytest so that the
    # computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
