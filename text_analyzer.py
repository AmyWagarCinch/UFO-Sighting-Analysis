def analyze_comment(comment):
#need to create a variable called text from the comment
    text = comment

    lines = text.splitlines()
    for line in lines:
        if len(line) == 0:
            lines.remove(line)

#move the paragraph out of the array and back into a string
    for line in lines:
        data = data + f' {line}'




#split on spaces to get words
    words = data.split()
    word_count = len(words)


#count letters to get average letters in a word
    letters = 0
    for word in words:
        letters += len(word)

    average_letters = letters/word_count

    return (word_count,average_letters)