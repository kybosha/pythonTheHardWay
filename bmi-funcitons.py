def divide(a, b):
        return a / b

def bmi():
        global weight
        global height
	weight = float(raw_input("What is your weight in Kilograms: "))
	height = float(raw_input("What is your height in Metres: "))
	return weight, height

def calculate_bmi(c, d):
        bmi = float(divide(divide(weight, height), height))
        return bmi
bmi()

bmi = calculate_bmi(weight, height)

def r_u_fat(e):
        if 18.5 > e:
                return "Underweight"
        elif 24.9 > e > 18.5:
                return "Normal Weight"
        elif 29.9 <= e:
                return "Overweight"
        else:
                return "Obese"

state = r_u_fat(bmi)

print "Your bmi is %d, this means that you are %r" % (bmi, state)