from datetime import datetime

# Prompt repository 
WELCOME_MESSAGE = "Greetings, visitor!! Welcome to a little preview of the website I want to build (eventually...). I want us to play a little game! I've made a cute little name generator that will assign you a unique economic persona (well, as unique as it can get with a finite number of economic systems and mathematical combinations)! All I need is your birthdate (I’m totally not an Astro girl), your choice of software, and a random letter from a book nearby (I would like to think that the venn diagram of people interested in me/my website and those interested in books is a circle). Sound good?"
YES_NO = "That was not a rhetorical question, I need a ‘Yes’ or ‘No’ in answer to this, please and thank you. "
YES = "Brilliant, let's proceed."
NO = "Well, sucks to be you I guess, because this is not optional. So let’s proceed!"
DATE = "To begin with, please enter your birthdate in a DD/MM/YYY format (Americans, kick rocks). "
SOFTWARE = "Next, I want you to pick your favourite software/language from this list: STATA, eViews, R, Python, MatLab, LaTex, MS-Excel, Julia, SPSS, SAS, SQL, NetLogo, FORTRAN, Mathematica, and C. If your favourite software is more niche, then congratulations on being special and unique! Choose your second favourite software!"
BOOK_LETTER = "So as I said earlier, I’d expect there to be at least one book around you. I want you to pick that up, flip to page 99, go to line 73, identify the 8th letter, and enter it here. If the 99th page is blank or there are only 15 lines on it, or whatever, just go to the next one…"
GOODBYE_MESSAGE = "Thank you for playing my game! Code in Place has been beyond magical; my only regret is wasting weeks trying to figure out tkinter and the kind of graphics I wanted, before giving up because I really wanted to submit this. Either way, I am so grateful for the opportunity! This has, unarguably, been ony of my favourite learning experiences. Before you leave, I have a joke for you!"
JOKE_QUESTION = "What is the heaviest thing in the Universe?"
JOKE_CORRECT = "Damn I got beaten in my own game. On that wonderful note (for you, I will sulk about this for eternity), goodbye! Have a nice life!!" 
JOKE_WRONG = "My eyelids while reading the methods section of a paper! I stole this joke off the internet, just so you know hehe. On that wonderful note, goodbye! Have a nice life!!"

# Dictionary repository
VALID_SOFTWARE: set[str] = ["stata", 
            "eviews", 
            "r", 
            "python", 
            "matlab", 
            "latex", 
            "ms excel", 
            "julia", 
            "spss", 
            "sas", 
            "sql", 
            "netlogo", 
            "fortran", 
            "mathematica", 
            "c"
]
ECONOMIST_NAME = {
        "1": "Hyman", #Minsky
        "2": "Carmen", #Reinhart
        "3": "Jon", #Danielsson
        "4": "Nassim", #Taleb
        "5": "Claudia", #Sahm
        "6": "Jordi", #Gali
        "7": "Viral", #Acharya
        "8": "Raghuram", #Rajan
        "9": "Frances", #Coppola
        "10": "John", #Keynes
        "11": "Karl", #Marx
        "12": "Douglas", #Diamond
}
ECONOMIC_SCHOOL = {
        "c": "MMT Thumper",
        "fortran": "Austrian",
        "julia": "Econophysicist",
        "latex": "Doughnut economist",
        "matlab": "Anarchist",
        "mathematica": "Complexity Lord",
        "ms excel": "Thermoeconomist",
        "netlogo": "New Keynesian",
        "python": "Monetarist",
        "r": "Marxian Economist",
        "sas": "Feminism Economist",
        "spss": "Mercantilist",
        "sql": "Neo-Classical",
        "stata": "Sraffian",
        "eviews": "Post-Keynesian", 
}
METRICS_CHARACTERISTIC = {
        "a": "Zero-summed",
        "b": "Volatile",
        "c": "Too big to fail",
        "d": "Systemically important",
        "e": "Shortsighted",
        "f": "Self-fulfilling",
        "g": "Representative",
        "h": "Pluralist",
        "i": "Perfectly identified",
        "j": "Pareto-optimal",
        "k": "Optimal",
        "l": "Morally hazardous",
        "m": "Loss-averse",
        "n": "Leading",
        "o": "Lagging",
        "p": "Irrational",
        "q": "Inconsistent",
        "r": "Incentivised",
        "s": "Heteroskedastic",
        "t": "Exuberant",
        "u": "Efficient",
        "v": "Dynamically stable",
        "w": "Countercyclical",
        "x": "Chi-squared",
        "y": "Biased",
        "z": "Adversally selected",
}


def main() -> None:
    welcome_visitors()

    # Generate persona
    month = get_user_birth_month()
    #print(f"Debug: month after get_user_birth_month = {month}")
    name = assign_name(month)
    #print(f"Debug: name = {name}")

    software = get_user_favorite_software()
    school = assign_school(software)

    book_letter = get_user_book_letter()
    characteristic = assign_characteristic(book_letter)

    # Display persona
    print(
        f"Very cool, your generated persona is {name}, the {characteristic} {school}."
    ) 
    #Display a joke
    print(GOODBYE_MESSAGE)
    user_input = str(input(JOKE_QUESTION).strip().lower())
    if user_input == "My eyelids while reading the methods section of a paper.":
        print (JOKE_CORRECT)
    else:
        print (JOKE_WRONG)


def welcome_visitors ():
    print(WELCOME_MESSAGE)
    user_input = str(input(YES_NO).strip().lower())
    if user_input == "yes":
        print (YES)
    else:
        print (NO)


def get_user_birth_month() -> int:
    while True:
        try:
            date_string = str(input(DATE))
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
            month: int = date_object.month
            return month
        except Exception as e:
            print(
                "My dude, the value you entered for the month isn't quite correct. Let's try that again."
            )

def assign_name (month: int) -> str: 
    return ECONOMIST_NAME.get(month, "Unknown")
    # print("Debug: ECONOMIST_NAME =", ECONOMIST_NAME)

def assign_name(month: int) -> str:
    #print(f"Debug: month = {month}, type = {type(month)}") 
    #print(f"Debug: ECONOMIST_NAME keys = {ECONOMIST_NAME.keys()}")
    result = ECONOMIST_NAME.get(str(month), "Unknown") #this function is not a a part of the debugging
    #print(f"Debug: result = {result}")
    return result

def get_user_favorite_software() -> str:
    while True:
        try:
            software = str(
                input(f"Choose one of the following: {VALID_SOFTWARE}\n").strip().lower()
            )
            if software in {item.lower() for item in VALID_SOFTWARE}:
                return software
            else:
                # raise errors, don't return!
                raise ValueError
        except ValueError:
            print(
                "As i said, an obscure choice of software is entirely your problem. Choose your second-favourite, in that case"
            )
            
def assign_school (software: str) -> str:
    """
    Assign an economic approach given software.
    """
    return ECONOMIC_SCHOOL.get(software, "Unknown")


def get_user_book_letter() -> str:
    """
    Getting user input on a random letter in the book closest to them.
    """
    while True:
        try:
            book_letter = input(BOOK_LETTER).strip().lower()
            if book_letter.isalpha() and len(book_letter) == 1:
                return book_letter
            else:
                raise ValueError
        except ValueError:
            print("I asked for a singular letter. Let's go again")
            
def assign_characteristic (book_letter: str) -> str:
    return METRICS_CHARACTERISTIC.get(book_letter, "Unknown")   
    

if __name__ == "__main__":
    main()