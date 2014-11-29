Spell Suggester
============


Spell Suggester:

    1) It reads the /usr/share/dict/words and stores in a SET (see data/__init__.py)

    2) words are imported to all of the Classes for to be accessible

    3) Made an assumption about the number of continous repeated charcters is not more than 2 and the input is adjusted accordingly by removing the extra characters. 

RepetitionGenerator:

    1) We generate all possible candidates by selecting 1 or more in repeated characters.

       Example: "jjoobb" will converted to ["jjoob", "jjobb", "jjob","joobb", "jobb", "job"....] 

VowelReplacer:

    1) In this Class we create another dict(consonet_word_map) to stores consontent to word mapping

        Example: "vowel" is converted to "vwl" => "vowel". This helps to speed up for run time processing.


How To Run:

    python main.py 
    
    It prompts with a "> " and waits for input.

    To generate test input go to test directory and run 
   
    python generate_words.py 
   
        it  generates input words from words in data

    For verifying on Auto generated input go to the test directory 
    
    python generate_words.py | python ../main.py > suggestions.txt
    
    It takes quite some time for it to run. Due to recursion depth with repetition generations by looking at suggestions.txt you can verify there is no "NO SUGGESTION" in the output.
