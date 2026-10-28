name = input("what is your name ").title().strip()
sub = input("What's the sub your learning ").title().strip()
def learning_message(name,sub) :
    return f"Hi, I'm {name}. I'm learning {sub}"
v = learning_message(name,sub)
print(v)