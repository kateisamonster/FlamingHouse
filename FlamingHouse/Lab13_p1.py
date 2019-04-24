#Lab 13 part 1
#Kate Adler, Michael Garber, Michael Lee

#Find a story and make a madlib out of it.  
#Link to the original story
#https://www.stltoday.com/news/national/florida-man-threatens-to-unleash-turtle-army-on-his-foes/article_1a1e0e5a-6b58-5392-9c50-7d23a8c3c610.amp.html

def mad_lib():
	"""play a mad lib game and print the results"""
	
    word_list = []
    get_words(word_list)
    base_story = ["\n\nOne ", " man picked an unusual strategy of ", 
        " people while yelling obscenities in front of different businesses on Tuesday.\n\nThomas Devaney Lane, 61, was arrested after police in ", 
        ", a small beachside town about 55 miles southeast of Orlando, said they received numerous disturbance calls about Lane, Fox 35 reported.  According to WKMG, Lane called himself a ",
        "  and said he would send his ", 
        " army to destroy everyone, police said.\n\nLane also made his way to the lobby of the police department, where he pounded on the walls and glass. He left, but officers found him nearby, where police said Lane called 911 and told the operator, \"I need to  ",
        " now or you will all be sorry you ", " with the saint,\" WKMG reported." ]
    
    print (base_story[0] + word_list[0] + base_story[1] + word_list[1] + base_story[2] + word_list[2] + base_story[3] + word_list[3] + base_story[4] + word_list[4] + base_story[5] + word_list[5] + base_story[6] + word_list[6] + base_story[7])
    


def get_words(word_list):
	"""collects word input from the user"""
	
    word = raw_input("Enter a State:  ")
    word_list.append(word)
    word = raw_input("Enter a verb ending with \'ing\':  ")
    word_list.append(word)
    word = raw_input("Enter a City:  ")
    word_list.append(word)
    word = raw_input("Enter a noun:  ")
    word_list.append(word)
    word = raw_input("Enter an animal:  ")
    word_list.append(word)
    word = raw_input("Enter a verb:  ")
    word_list.append(word)
    word = raw_input("Enter a past tense of a verb:  ")
    word_list.append(word)

