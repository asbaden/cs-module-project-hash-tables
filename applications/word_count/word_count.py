
    #Plan
    # will need a dictionary to place the words and their counts 
    # iterate through the the string to keep a count of vvords
    # sort the dictionary by the value 

    #lower case everything 
    #handle special characters 

things_to_go = ['"', ':', ';', ',', '.','-', '+', '=', '/', '\\', '|', '[', ']', '{', '}','(', ')', '*', '^', '&']


def word_count(s):
    # Your code here
    # takes a single argument and returns a  dictionary of words and their counts
    counts = {}
    words = s.split()
    #Plan
    for word in words:
        word = word.lower()
        
        for i in things_to_go:
            # print("this is word before", word)
            word = word.replace(i, '')
            # print("this is word after", word)
        if word == '':
            return {}
        
        if word in counts:
            counts[word] += 1 
        else:
            counts[word] = 1 
    print(counts)
    return counts





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count("Hello    hello"))
    print(word_count(':;,.-+=/\\|[]{}()*^&"'))
    print(word_count("a a\ra\na\ta \t\r\n"))