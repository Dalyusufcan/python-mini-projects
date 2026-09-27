def calculate_bmi(weight, height):
    return (weight/(height**2))


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Fazla kilolu"
    else:
        return "Obezite aralığı"