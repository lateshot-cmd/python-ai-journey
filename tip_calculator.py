billamt = float(input("What's your bill? "))
tipperc = float(input("What's your tip percentage? "))
def calculate_tip(billamt,tipperc) :
    return billamt * tipperc/100
tipamt = calculate_tip(billamt,tipperc)
total = billamt + tipamt
print(f"Tipamt: {tipamt:,.2f}")
print(f"Totalamt: {total:,.2f}")