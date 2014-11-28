DisqusCoding
============

Spell Suggester:

    1) It reads the /usr/share/dict/words and stores in a SET (see data/__init__.py)

    2) words are imported to all of the Classes for to be accessible

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
   
    python generate_input.py 
   
        it  generates input words from words in data

    Inside the test directory 
    python generate_input.py | python ../main.py > suggestions.txt
    
        It takes quite some time for it to run. Due to recursion depth with repetition generations by looking at suggestions.txt you can verify there is no "NO SUGGESTION" in the output.
