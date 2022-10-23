import random,time
count = 0
start_time = time.time()
character = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@£#$%^&*()_-+=[{]}:;|'~`?!"
character_list= list(character)
password = input ("Enter your password:")
guess = ""

while (guess != password):
    guess = random.choices(character_list, k=len(password))
    count += 1
    print(guess)
    guess = "". join(guess)
    print (guess)

if guess == password:
    print("Your password is " + guess)
    print("It took %s seconds --- to crack your password!" % (time.time() - start_time))
    print("It took a total of:",count , "combinations, consisting of words, numbers and symbols to crack your password!")
