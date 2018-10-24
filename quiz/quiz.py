def show_menu():
    #play game - ask questions
    print("1. Ask questions")
    #add questions and answers
    print("2. Add a question")
    
    #quit game
    print("3. exit game")
    
    #option variable using input function
    option = input ("Enter option: ")   
    
    return option
    
    
#The last part of our game that we need to write is the actual quiz itself, and we're going to do this incrementally. Maybe we'll start by loading the questions from the file and asking them but ignoring the answers. Then, a little bit later, we'll add answer checking and score-keeping. Let's go ahead and add our ask_questions() function. We'll begin by creating two empty lists, one for the questions and another one for the answers.     

def ask_questions():
    questions = []
    answers = []
    
#Now, we're going to use a slightly different method of opening our file this time. Instead of the method that we've learnt already, we're going to use a with block. There are many reasons for using this, which are good in general development. As you can see, the syntax is very similar. We're opening it with the 'read' access mode flag as file. The handy thing about the with block is that it handles a lot of stuff for us. For instance, we don't need to worry about closing the file because at the end of the width block it will be closed.    

#The next thing that we're going to do then is to use the enumerate function. The enumerate function is going to turn each of these lists into a tuple with a line number stored in 'i' and the text in 'text'. So, if 'i' is even - if the line number is even - then we say that that's a question. If it's odd, then that's going to be an answer. Let's just think about how that works for a minute. We know that the first line of our questions.txt file was the question, which is line 0, so that's classed as even and then line one would be odd. Our questions and our answers get appended into the two lists. 

    with open ("questions.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
                
        else:
            answers.append(text)
    

#et's go ahead now and add in the functionality to check the answers and also to keep score. So, here now we need to know the number of questions that there are in our file. We do that by checking the length of our questions list.
    number_of_questions = len(questions)
    
    questions_and_answers = zip(questions, answers)
    
    #  And, finally, we'll initialize an empty variable called score, which at the beginning, of course, is set to zero. 
    
    score = 0
    
    for question, answer in (questions_and_answers):
    #for question, answer in zip(questions, answers):
        guess = input(question + "> ")
        
    #Now, instead of the zip function, we go through our questions and answers list. Our guess can stay the same, but now we need to check to make sure that the answer is correct. So, if our guess is equal to our answer then it's correct and we add 1 to the score. We then print that we were right, and we'll also then print the score as well just so we can keep track of what's going on. If we get the answer wrong then we're just going to print 'wrong'.  
    
    if guess == answer:
        score += 1
        print ("right!")
        print (score)
    else:
        print ("wrong!")
       
   #And, finally, when the whole loop has run round and we've gone through every single one of our questions and answers, then we can print that you got so many correct (spell 'out' correctly) out of so many, and we'll use our format method again. This time, we pass in our score and the total number of questions. So, it will say you got so many correct out of the total number of questions. So, this makes sense. You can see that we're incrementing the score. We can see that we've got a right and a wrong message. Let's save it. We'll run it again and check that it works. python3 quiz.py Option 1. What is the capital of Ireland? Dublin. It says that's right, 1, and we got 1 correct out of 1. So, let's just add another question. What is the capital of France? The answer is Paris and when we ask now, we get our first question up. Dublin, which is right. Let's try giving it a wrong answer. See what happens? We get 'wrong', and then it tells us that we've got one correct out of two. That concludes our lesson on Python file handling. We've looked at two different methods for opening files, and we've examined the various different file access modes that are available to us in Python. We've also looked at the different functions that can enumerate and join together lists. So, before moving on maybe think about ways that you could improve this game - perhaps by random question choice or even the ability to delete a question. File handling is an important part of any programming language, so you've come a long way here with Python. Don't forget to add and commit your code to GitHub before moving on to the next lesson.   
   
    print ("You got {0} correct out of {1}".format(score, number_of_questions))
        
#Then, we're going to use questions and answers here as another variable and we're going to call the zip function on this. This prevents us having to run the zip function every time the for loop is run.        
   
    #questions_and_answers = zip(questions, answers)
    
    
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
        
#Let's just add in the functionality to actually get it working from our menu. We put the ask_questions() function there, and then talk for a minute about exactly what's going on here. So, as we said, we use the with block; we open the questions.txt; we use the enumerate function, which creates a tuple in memory with a line number at the beginning, which we represent with 'i' and then the text. We check to see whether the line numbers are even or odd and we put them into questions or answers, and then, finally, we use a zip function to put everything together into another tuple in memory, and this looks like this. This is what we're left with - a tuple that contains a question and our answer, a question and our answer. So, we can easily check the answer from our question because the two are related. They're effectively two columns of text. Let's just check to see that this works then.  So, we'll select option 1 to ask a question: What is the capital of Ireland? The answer is Dublin. So it asks a question - ok, at the moment, it's discarding the answer - but we can see that our question asking part is working. 
        
        option = show_menu()
        if option == "1":
            #we don't as yet have the functionality to ask questions, so just do this.
            #this is now our functionality.
            ask_questions()
            #print("You selected 'Ask Questions'")
        elif option == "2":
                #we still don't have functionality to add a questions, so just do this.
        
            add_question()

            print("You selected 'Add a Question")
                
#Now, all we need to do to actually get it working is to call the function from inside our game loop if the user chooses option 2. We can get rid of our print statement here, and run the add_question() function. Now, when the user selects option 2 then the add_question() function that we just created will be called and we'll be prompted for a question and an answer. Okay, very good. Let's save that and try running it and we'll see if we can add a question into the questions.txt file. python3 quiz.py. This time, option 2. So, enter a question. We'll type it properly. 'What is the capital of Ireland?' And, you see there that it prompts us then with the question. The answer is 'Dublin'. So, now that's been added let's exit the game. Using the 'cat' command, which is part of Linux, to list the contents of a file, we'll look at what's in questions.txt. We see our question and our answer on separate lines. So, now that we've got that working, in our next video we'll finish off the game by looking at how to ask questions and how to keep score.
        
        elif option =="3":
                break
        else:
                print("Invalid Option")
                
        print("")
#we'll call the game loop, we've a game loop function here and will continue running forever
game_loop()
            