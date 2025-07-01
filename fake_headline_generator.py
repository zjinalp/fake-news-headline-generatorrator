# import random module
import random

# subjects
subjects = ["President", "Influencer", "CEO", "Doctor", "YouTuber", "Billionaire","Celebrity", "Hacker", "Politician","NASA", "Google", "WHO", "Parliament", "School Kids", "Protestors","Secret Society", "Startup Company", "Anonymous Hackers", "Alien Council" "AI Robot","Dog", "AI Assistant", "Drone", "Self-Driving Car", "Monkey", "Smart Fridge","UFO", "Talking Parrot", "Robot Vacuum", "Ghost"]

actions = ["Declares war on", "Announces partnership with", "Claims responsibility for","Warns against", "Demands apology from", "Promises free access to","Blames others for", "Vows to destroy", "Denies involvement in", "Declares independence from","Caught stealing", "Found dancing", "Goes missing", "Seen crying", "Gets hacked","Quits suddenly", "Files lawsuit", "Starts fire", "Breaks silence on", "Flees country after","Marries AI", "Talks to ghosts", "Smells like chicken", "Turns into a meme","Bans laughter", "Trains pigeons to spy","Declares Monday illegal","Claims Earth is triangle-shaped", "Buys the moon", "Challenges aliens to rap battle"]

objects = ["in Antarctica", "at Mars base", "inside White House", "in local zoo", "under the sea","on a TikTok live", "at Hogwarts", "in parallel universe", "at secret island", "on flying train","about banana shortage","over AI rights", "during meditation", "regarding flying cars","over cloned cats", "about flat Earth", "with invisible ink", "involving time machine","with lava-powered engine", "about onion prices","during peace summit", "in cooking contest", "while robbing a bank", "at climate protest",
 "during alien invasion", "after losing chess match", "at midnight ritual","before stock market crash", "during full moon eclipse", "after 100-hour livestream"]

# headline generation while loop

while True:
    subjects_choice = random.choice(subjects)
    actions_choice = random.choice(actions)
    objects_choice = random.choice(objects)

    headline = f"Breaking News : {subjects_choice} {actions_choice} {objects_choice}"

    print("\n" + headline)

    user_input = input("\n Do you want another headline ? (Yes/No)").strip().lower()

    if user_input == "no":
        break

print("Thanks for using this website ...!!!")