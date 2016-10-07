import random

responses = ["Unfortunately, today is just not your day.", "Absolutely, and sooner than you might expect!", "The spirits are silent. Try again another time.", "You have GOT to be kidding me!", "Okay, I thought I'd heard everything, but that is one strange question.", "I think you've been watching too many episodes of CSI.", "I wouldn't if I were you.", "Yes, absolutely, one hundred percent!", "Do you kiss your mother with that mouth?!", "You're definitely on the right track. Keep it up!", "No way, Jose!", "No comment. I'm not touching that one.", "You can't possibly be serious.", "Well, of course! What did you THINK would happen?", "Ask me again during the commercial break. I really want to see this part.", "You can't ask questions like that before I've had my first cup of coffee.", "I guess so. I'm feeling generous.", "Did you just say that out loud??"]

selection = random.choice(responses)
answer = selection

question = raw_input("Ask any question of the Omnipotent Olivia Onyx O'Reilly! Learn the answers to the mysteries of the universe, or just find out where you left your car keys.\n")
print answer
question = raw_input("\nYour session includes two more questions. Enter another question, or enter no to end your fortune-telling session.\n")
selection = random.choice(responses)
result = selection
if question != "no":
    print result
    question = raw_input("\nAsk your third and last question, or enter no to end your session.\n")
    selection = random.choice(responses)
    conclusion = selection
    if question != "no":
        print conclusion
        print ("\nI hope you are pleased with the knowledge that you have been granted. Thank you for communing with the spirits. May your most heartfelt wishes come true!\n")
    else:
        print ("\nThank you for communing with the spirits. May all of your questions be answered, and all of your dreams come true!\n")
else: print ("Thank you for communing with the spirits. May all of your questions be answered, and all of your dreams come true!")
