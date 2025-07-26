temperature = int(input("Input the temperature (≥ 0): "))

if temperature > 35:
    print("It’s a very hot day! 🔥")
elif temperature > 25:
    print("It’s a warm day! 🌤️")
elif temperature > 15:
    print("It’s a cool day! 🍃")
else:
    print("It’s a cold day! ❄️")
