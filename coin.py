import random 

head = 0
tail = 0
current_coin = ""
for i in range(1,101):
    random_num = random.random()
    if round(random_num) == 1:
        head += 1
        current_coin = "head"
    elif round(random_num) == 0:
        tail += 1
        current_coin = "tail"
    print "Attempt #" + str(i) + ": Throwing a coin... It's a " + current_coin + "! ... Got " + str(head) + " head(s) so far and " + str(tail) + " tails(s) so far"
print "Ending the program, thank you!"
