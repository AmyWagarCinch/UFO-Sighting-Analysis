#defining a function to do the analysis
#pass in a string
#returns a tuple of the word count and average word length
def analyze_comment(comment):
#need to create a variable called text from the comment
    text = str(comment)

    lines = text.splitlines()
    for line in lines:
        if len(line) == 0:
            lines.remove(line)

#move the paragraph out of the array and back into a string
    long_string = ''
    for line in lines:
        long_string = long_string + f' {line}'




#split on spaces to get words
    words = long_string.split()
    word_count = len(words)


#count letters to get average letters in a word
    letters = 0
    for word in words:
        letters += len(word)

    average_letters = letters/word_count

    return (word_count,average_letters)