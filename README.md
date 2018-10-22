# Walkthrough Project: Quiz Game

## What is it?

An example of a quiz game.

## What does it do?

It uses all of the techniques we've learned in the file I/O section to create a quiz game that asks questions, keeps score and allows us to add new questions and answers.

## How do you use it?

Follow the walkthrough project on your own computer and try the challenge at the end.

LESSON:

Now, let's use all the things that we've learned to create a simple quiz game. So,
our game will store questions and answers in a file. When you run it, it will ask
the questions and check your answers against those in the file. At the end of
the quiz, it will tell you how many questions you got right. It will also
allow us to add new questions and answers to our quiz file. When we run the
game, we will be presented with a menu with the following options: the first option
to ask questions; the second to add a question; and the third to exit the game.
If you select option 1 to ask questions, the game will display each quiz question
in turn, asking for the answer to each one. When you give an answer, the game
will indicate whether it's right or wrong before moving to the next question.
After all of the questions have been answered, the game will display how many
out of the total number of questions asked that you got right.
It will then return to the main menu. If we select option 2 to add a question, the
game will prompt the user for the question and the answer, and it will
append these to the questions file. It will then return to the main menu. Finally, if
we choose option 3 then the game will simply shut down.

# Walkthrough Project - Part One

## What is it?

An example of a quiz game.


## What does it do?

It uses all of the techniques we've learned in the file I/O section to create a quiz game that asks questions, keeps score and allows us to add new questions and answers.


## How do you use it?

Follow the walkthrough project on your own computer and try the challenge at the end.

LESSON: 

So, let's get started. I'm going to create a new folder called 'quiz' to store our
files in and, in there, I'm going to create a new, empty file and call it
questions.txt. We're not actually going to fill that file with questions
now. Instead, we're going to write the code that allows us to add questions.
Now, I'm going to create the actual game file which we'll call quiz.py. Let's open
that file up and begin by building a very simple game menu. So, we'll call this
function show_menu() and we'll print out our menu options. The first one is to
play the game - to ask questions. The second option is going to be to add
questions and answers to our file, and then the third option is going to be to
quit the game. We're then going to have an option variable, where we use the
input function to get the text. The prompt is going to be 'Enter option', and
our function is just going to return whatever option the user selects. Let's
test that. We'll use a print function to call it and, if we open a terminal window
here, (change into our quiz directory first of all) and now: python3 quiz.py
We can see that our menu works. When we select option 2, it prints that
option to screen just as we would expect. So, our simple menu is working. The next
thing to do, then, is to create the actual game loop itself. We're going to create a
loop that continues as long as we keep playing the game. When option 3 is selected,
we'll break out of the loop and the game quits. So, we'll call this new function
game_loop() We'll put 'while true'. This is just a shortcut for basically saying
loop forever unless there's a break, because we're not actually checking a
condition here. So, now we'll call our show menu
function and store whatever option was chosen in the option variable. So, if our
option is equal to one, just for now, let's say 'You selected ask questions'
because we don't yet have the functionality to ask a question. You use
the' elif' and say that, if we chose option two instead, then we still don't
have the function to add a question, so let's just say 'You selected add a
question'. And, finally, if we have option three this is easier we can actually
quit from the game just by using break. That will break us out of our loop. And,
finally, we just need some checking here in case somebody puts anything other
than 1, 2 or 3. So, we'll print 'Invalid option'. Then, after
everything, we're going to print a blank line just to make things look a little
bit nicer. Now, we'll call the game loop with the game_loop() function here, and it
will just continue running forever. Let's test it again. So, now, if we select
option 1...yep, 'You selected ask questions'.
Option 2: 'You selected add a question'.
Put 5...yep, 'Invalid option' - so, that works.
And, then, 3 quits.
So, now that we have that working let's actually add the option to add a question to our file.
We want to be prompted for a question and answer, and then we want
both of them to be appended to the questions.txt file. So, let's create a new
function. We'll add it just below our menu function, and we'll call it add_question().
So, first of all, let's print a blank line again and then our question
prompt. We're going to store it in a question variable. Again, we'll use input
and our prompt will be: 'Enter a question'. We'll put a new line here, and then a
greater-than sign as a prompt, and a space just to make it look nice.
And, once we've inputted, we'll print another blank line. Then,
we'll say: 'OK then, tell me the answer'. So, again, we'll store this in the answer
variable. We'll use an input. This time, we'll take the question that we'd
already asked, do a blank line, a greater-than sign for a prompt and then, using
the format method, we'll insert the question there. So, now the user will be
asked the question again when they come to put the answer in. Now, we get on to
the part where we actually add this to the file. We'll open our questions.txt
file for appending using the 'a' access mode flag. The first thing we'll do is
write our question, and then we'll add a new line at the end. The second thing
we'll do, then, is write our answer, and we'll add a new line at the end. So, each
question and answer will go on its own line. Finally, we'll close the file. So,
that function works nicely. Now, all we need to do to actually get it working is
to call the function from inside our game loop if the user chooses option 2.
We can get rid of our print statement here, and run the add_question()
function. Now, when the user selects option 2 then the add_question()
function that we just created will be called and we'll be prompted for a
question and an answer. Okay, very good. Let's save that and try running it
and we'll see if we can add a question into the questions.txt file.
python3 quiz.py. This time, option 2. So, enter a question. We'll type it properly :)
'What is the capital of Ireland?'
And, you see there that it prompts us then with the question.
The answer is 'Dublin'. So, now that's been added let's exit the game. Using
the 'cat' command, which is part of Linux, to list the
contents of a file, we'll look at what's in questions.txt.
We see our question and our answer on separate lines. So, now that we've got
that working, in our next video we'll finish off the game by looking at how to
ask questions and how to keep score.
