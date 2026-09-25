def recommendation(temp):
    if temp<32:
        print("Be sure to wear thermal underwear and a hat!")

    elif temp>=32 and temp<=50:
        print("Wear your winter coat")

    elif temp>=51 and temp<=70:
        print("You may want a light jacket")

    else:
        print("Wear shorts!")

def main():
    temperature=int(input("What is the temperature outside?"))
    recommendation(temperature)

main()
