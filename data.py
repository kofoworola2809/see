# A = True 
# B = False

# print("A and B:", A and B) #False

# print("A or B:", A or B) #True

# print("not A:", not A)  #False

# print("A ^ B:", A ^ B)


def logic_simulator(a, b):
    print("A AND B:", a and b)
    print("A OR B:", a or b)
    print("NOT A:", not a)
    print("A XOR B:", a ^ b)
logic_simulator(True, False)

email_valid = True
password_correct = True

if email_valid and password_correct:
    print("login successful")

else:
    print("login failed")