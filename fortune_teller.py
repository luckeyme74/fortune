import random

responses = ["Unfortunately, today is just not your day.", "Absolutely, and sooner than you might expect!", "The spirits are silent. Try again another time.", "You have GOT to be kidding me!", "Okay, I thought I'd heard everything, but that is one strange question.", "I think you've been watching too many episodes of CSI.", "I wouldn't if I were you.", "Yes, absolutely, one hundred percent!", "Do you kiss your mother with that mouth?!", "You're definitely on the right track. Keep it up!", "No way, Jose!", "No comment. I'm not touching that one.", "You can't possibly be serious.", "Well, of course! What did you THINK would happen?", "Ask me again during the commercial break. I really want to see this part.", "You can't ask questions like that before I've had my first cup of coffee.", "I guess so. I'm feeling generous.", "Did you just say that out loud??"]

selection = random.choice(responses)
answer = selection

question = raw_input("Ask any question of the Omnipotent Olivia Onyx O'Reilly! ")
print answer
