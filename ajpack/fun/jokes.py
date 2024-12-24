import random

def joke() -> None:
    """
    Tells a joke.
    """
    predefinedJokes: dict[str, str] = {
        "Why do programmers prefer dark mode?":" Because the light attracts bugs!",
        "Why do Java developers wear glasses?": "Because they don't C#.",
        "How many programmers does it take to change a light bulb?": "None. That's a hardware problem.",
        "Why do Python programmers have low self-esteem?": "Because they constantly compare themselves to others.",
        "Why was the JavaScript developer sad?": "Because he didn't know how to 'null' his feelings.",
        "Why did the programmer quit his job?": "Because he didn't get arrays.",
        "What do you call a programmer from Finland?": "Nerdic",
        "Why did the developer go broke?": "Because he used up all his cache.",
        "How do you comfort a JavaScript bug?": "You console it.",
        "Why do C++ programmers have trouble dating?": "Because they have too many pointers.",
        "What do you get if you cross a cat with a dark web developer?": "A purrly coded website.",
        "Why don't programmers like nature?": "It has too many bugs.",
        "What did the Java code say to the C code?": "You've got no class.",
        "Why was the computer cold?": "It left its Windows open.",
        "Why can't SQL and NoSQL be friends?": "They always argue over relationships.",
        "How do you know if a programmer has had too much coffee?": "They keep hitting F5 because they're looking for a refresh.",
        "Why do Python programmers hate shopping?": "Because they hate the index error.",
        "Why do programmers love nature?": "It's full of trees.",
        "What's a programmer's favorite type of music?": "Algo-rhythm.",
        "Why do functions always break up?": "Because they have too many arguments.",
        "What do you call 8 Hobbits?": "A Hobbyte.",
        "Why did the programmer go to the doctor?": "Because he had a virus and couldn't 'debug' it.",
        "Why did the administrator leave his wife?": "Because she had one-too-many relationships.",
        "Why was the computer squeaking?": "Because someone stepped on its mouse.",
        "What is a programmers favourite type of humor?": "Something that isn't 'byte'-ing.",
        "Why do coders hat the dark?": "Because they can't C#.",
        "Why did the web developer drown?": "He didn't know how to 'float'.",
    }

    # Choose a joke
    randomJokeKey: str = random.choice(list(predefinedJokes.keys()))

    # Print the joke
    print(f"{randomJokeKey}\n-> {predefinedJokes[randomJokeKey]}")
