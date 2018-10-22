def show_menu():
    #play game - ask questions
    print("1. Ask questions")
    #add questions and answers
    print("2. Add a Question")
    
    #quit game
    print("3. Exit Game")
    
    #option variable using input function
    option = input ("Enter option: ")   
    
    return option
    
    
#So, now that we have that working let's actually add the option to add a question to our file. We want to be prompted for a question and answer, and then we want both of them to be appended to the questions.txt file. So, let's create a new function. We'll add it just below our menu function, and we'll call it add_question().  So, first of all, let's print a blank line again and then our question prompt. We're going to store it in a question variable. Again, we'll use input and our prompt will be: 'Enter a question'. We'll put a new line here, and then a greater-than sign as a prompt, and a space just to make it look nice.
def add_question():
    print("")
    question = input("Enter a Question\n> ")

    print("")
    print("Ok then, tell me the answer")
    
#So again, we'll store this in the answer variable. We'll use an input. This time, we'll take the question that we'd already asked, do a blank line, a greater-than sign for a prompt and then, using the format method, we'll insert the question there. So, now the user will be asked the question again when they come to put the answer in.    
    answer = input("{0}\n> ".format(question))
    
#ow, we get on to the part where we actually add this to the file. We'll open our questions.txt file for appending using the 'a' access mode flag. The first thing we'll do is write our question, and then we'll add a new line at the end. The second thing we'll do, then, is write our answer, and we'll add a new line at the end. So, each question and answer will go on its own line. Finally, we'll close the file. So, that function works nicely. 
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write (answer + "\n")



    #lets test it, use print functiont to call it.
#print(show_menu())

def game_loop():
    #just another way to say loop forever.
    while True:
        option = show_menu()
        if option == "1":
            #we don't as yet have the functionality to ask questions, so just do this.
            print("You selected 'Ask Questions'")
        elif option == "2":
                #we still don't have functionality to add a questions, so just do this.
        
                #print("You selected 'Add a Question")
                
#Now, all we need to do to actually get it working is to call the function from inside our game loop if the user chooses option 2. We can get rid of our print statement here, and run the add_question() function. Now, when the user selects option 2 then the add_question() function that we just created will be called and we'll be prompted for a question and an answer. Okay, very good. Let's save that and try running it and we'll see if we can add a question into the questions.txt file. python3 quiz.py. This time, option 2. So, enter a question. We'll type it properly. 'What is the capital of Ireland?' And, you see there that it prompts us then with the question. The answer is 'Dublin'. So, now that's been added let's exit the game. Using the 'cat' command, which is part of Linux, to list the contents of a file, we'll look at what's in questions.txt. We see our question and our answer on separate lines. So, now that we've got that working, in our next video we'll finish off the game by looking at how to ask questions and how to keep score.
            add_question()

        elif option =="3":
                break
        else:
                print("Invalid Option")
                
        print("")
#we'll call the game loop, we've a game loop function here and will continue running forever
game_loop()
            