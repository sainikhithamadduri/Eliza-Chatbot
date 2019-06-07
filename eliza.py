
# coding: utf-8

# In[22]:



# Introduction :


#Authors : Merin Joy and Sai Nikitha
#Date : 19th September 2018
#The following Eliza program acts as a psychotherapist that engages in conversation with the user. By making use of NLTK and 
#regular expressions.


# Instructions to run :


#Step 1: Run the following code in command line or ipython notebook.
#Step 2: Type in English and start the conversation by providing your Name.
#Step 3: Continue the conversation by replying to the pre-defined statements.
#Step 4: End the conversation by typing quit.


# Example Conversation :


#Talk to me by typing in English. Enter quit when you are done.
#--------------------------------------------------------------
#Hello. I am a Psychotherapist. Whom do I have the pleasure of speaking with?
#Hello.I am Merin
#Hi  Merin. What brings you here?
#>I need assistance
 #Merin How important is assistance to you?
#>It is very important to me
#Please tell me more
#>I feel depressed
#Have you discussed your issues with someone?
#>Yes
#Why do you say yes?
#>I have discussed it with my parents
#Good family relations are extremely important.
#>Are you a machine?
#I might be a machine?, what do you think?
#>i think you are a bot
#When did you get that thought?
#>While talking to you
#And how does it sound to you?
#>Its weird
#Tell me about your closed ones?
#>I am close to my faamily and friends
#Are you happy with them?
#>Yes
#Please tell me more
#>My parents are good individuals
#How do you feel about them?
#>Amazing!
#Why do you say amazing?
#>Because they are!
#Are you sure?
#>Yes
#Please tell me more
#>Okay its time to go! bye!
#Sounds good
#>quit
#Your bill will be sent to your mail.


# Algorithm :


#Step 1: Start
#Step 2: Extract the input string.
#Step 3: Check if input string matches equals to quit
    #Step 3.1: Then return
#Step 4: Else
    #Step 4.1: Extracting the input string that matches the regular expression
    #Step 4.2: Calling function pairs with argument as input
    #Step 4.3: Start the conversation
#Step 5: End



# In[23]:


#import chat util class from nltk library along with built-in reflections
from nltk.chat.util import Chat, reflections

# import built-in python regular expressions library 
import re

# These are nltk built-in reflections which are used for custom word-to-word mapping while framing responses
reflections


# In[24]:


# get_pairs function takes in the users name as input and returns pre-defined mapping(Python tuple) 
# of user answers to their succeeding questions
def get_pairs(name):
    
    # First argument is the regular expression, followed by pre-defined set of replies.
    pairs = (
        
        # Dangerous and impulsive words
        (r'(.*)((K|k)ill|(S|s)uicide|(H|h)omicide|(M|m)urder|(D|d)eath|(S|s)lay)(.*)',
        ("What makes you say that?",
        "I think you need serious attention and care.",
         "Please call the prevention lifeline at 1-800-273-8255",
         "Please listen to me and calm down.",
        "I think its an emergency. I am dailing 911!")),
        
        # Therapy and counseling words
        (r'(.*)((P|p)rocess|(C|c)ounselor|(P|p)sychologist|(S|s)ocial worker|(P|p)sychotherapist|(T|t)herapist)(.*)',
        ("Have you seen a counselor before?",
        "Have you discussed your issues with someone?",
         "What do you expect from the counseling process?",
         "Do you want to talk about your issues?")),
        
        # Problematic words
        (r'(.*)((P|p)roblem|(I|i)ssue|(D|d)epress|(H|h)ate|(B|b)ull(ied|y))(.*)',
        ("What is the problem from your viewpoint?",
        "Have you discussed your issues with someone?",
         "How does this problem make you feel?",
         "What makes the problem better?")),
        
        # Relationships
        (r'(.*)((B|b)oyfriend|(G|g)irlfriend|(F|f)riend|(F|f)amily|(R|r)elative|(P|p)eople)(.*)',
        ("How often do you get to meet up them?",
         "Do you have someone to talk to?",
         "Are you happy with them?",
         "Is there anyone who you feel understands you and is close to you?",
         "What involvement do you have with them?")),
        
        (r'(.*)(P|p)arent(.*)',
         ("Tell me more about your parents?",
          "How do you feel about them?",
          "How strong is your relationship with them?",
          "Good family relations are extremely important.")),
 
        [r'(.*)(C|c)hild(.*)',
         ["Did you have a childhood best friend?",
          "What is your favorite childhood memory?",
          "Did you get bullied as a child?"]],
        
        # Life
        (r'(.*)(L|l)ife(.*)',
        ("What choice do you have about what happens in your life?",
        "Do you have a clear sense of where you want to take things in life?",
         "Do you feel excited by stuff in your life?")),
        
        # Mind, Body and Health
        (r'(.*)((D|d)iet|(S|s)leep|(E|e)xercise|(H|h)ealth|(B|b)ody)(.*)',
        ("Are you sleeping these days?",
        "Are you happy with your diet?",
         "How much exercise are you getting?")),
        
        # Statements about machines or code
        (r'((C|c)omputer |(R|r)obot |(B|b)ot |(M|m)achine |(C|c)reate)(.*)',
        ("Are you talking about me?",
         "My name is Eliza and I am here to help you!",
         "How do you feel speaking to a robotic Psychotherapist?",
        "Do you like machines?")),
        
        # Starting with I
        (r'(I|i) need (.*)',
        (name+" Why do you need %2?",
        name+" How important is %2 to you?",
        name+" Are you sure you need %2?")),

        (r'(I|i) feel (.*)',
        ( "Why "+name+" are you feeling %2?",
        name+" How often do you feel %2",
        name+" What do you do when you feel %2?",
        "Is there anything I can do to make you feel better?")),

        (r'(I|i) want (.*)',
        ( "Why do you want %2?",
        "Will you be happy if you get %2?")),

        (r'(I|i) would (.*)',
        ( "Why would you %2?",
        "Is anyone aware that you would %2?")),
        
        (r'(I|i) will (.*)',
        ("Are you sure you will %2",
        "Are you sure that you want to do it",
        "I encourage you to do good and useful things")),

        (r'(I|i) think (.*)',
        ("Why do you think %2?",
        "When did you get that thought?")),

        (r'(I|i) can\'t (.*)',
        ( "Why you can't %2?",
        "How do you know you can't %2?",
        "I think you can %2 if you try")), 
        
        # Asking questions
        (r'(C|c)an you (.*)',
        ( "Sure I am here to help you out.",
        "I will try my level best %2?",
        "If I cant then what will you do?")), 

        (r'(A|a)re you (.*)',
        ( "You think I am %2?",
        "How does that bother you?",
        "I might be %2, what do you think?")),

        (r'(.*)(W|w)hat (.*)',
        ( "Why do you want to know?",
        "How important is it for you to know?")),

        (r'(Y|y)ou are (.*)',
        ("You think I'm %2",
        "I think you are talking about yourself?",
        "How can you say that?")),
        
        # Reasoning statements
        (r'(.*)(B|b)ecause (.*)',
        ( "Are you sure?",
        "Are there any other reasons for it?")),
        
        # Apology statements
        (r'(.*)((S|s)orry |(A|a)polog)(.*)',
        ( "Thats fine, I can understand.",
        "No problem.",
        "Its totally fine")),
        
        # Acknowlegdements
        (r'(.*)(T|t)hank (.*)',
        ( "You are welcome!",
         "Sure. No worries!",
        "Do you need any other help?")),

        (r'(Y|y)es (.*)',
        ("You seem confident",
         "I understand.",
        "Looks like you are confident about it",
         "Okay, so tell me more.",
        "I will recommend you to concerned doctor. He shall help you out with it.")),
        
        (r'((S|s)ure |(O|o)kay|(R|r)ight)(.*)',
        ("Great! So, tell me more about yourself",
         "Alright. Good luck",
        "Sounds good")), 

        (r'(N|n)o (.*)',
        ("If you dont want to,its fine",
        "You are confident about it?",
         "Okay, so tell me more about yourself."
         "Alright.",
        "Do you want to think about it?")),

        # Statements for quiting
        (r'((Q|q)uit|(B|b)ye(.*))',
        ("Thank you for consulting me.",
         "Good-bye and take care.",
         "Your bill will be sent to your mail.",
         "Take care and have a great day!")),
        
        # Default statements
        (r'(.*)',
        ( "Please tell me more",
         "Care to explain that?",
         "Tell me about your closed ones?",
         "Can you elaborate on that?",
         "And how does it sound to you?",
         "Why do you say %1?",
         "I see.",
         "How do you feel when you say that?"))

        
    )
    return pairs


# In[25]:


# eliza function creates a Chat instance imported from nltk and engages the user in a converstion taking
# his/her input from keyboard
def eliza():
    print("Talk to me by typing in English. Enter quit when you are done.")
    print('-'*62)
    print("Hello. I am a Psychotherapist. Whom do I have the pleasure of speaking with?")
    
    # extracting user name using regular expressions
    my_input = input()
    
    # when input matches quit
    if re.match(r'(Q|q)uit', my_input) is not None:
        return
    
    # when input is not quit
    else:
        match_obj = re.match(r'(Hi.|Hello.)?(My name is|Hi|I am|Myself|This is)?(.*)', my_input, re.I)
        name = match_obj.group(3)
        print("Hi",name +". What brings you here?")

        #get question and answer pairs required for chat instance creation
        pairs = get_pairs(name)
        # create the chat instance by passing pairs and reflections
        eliza_chat = Chat(pairs, reflections)
        #start conversation 
        eliza_chat.converse()


# In[26]:


eliza()

