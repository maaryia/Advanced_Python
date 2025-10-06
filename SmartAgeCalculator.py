from datetime import datetime

class Agecalculate:
    def __init__(self, birth):
        self.birth = birth
    
    def calculate_age(self):
        try:
            birth_date = datetime.strptime(self.birth, "%Y/%m/%d")
            today = datetime.now()

            age = today.year - birth_date.year

            if(today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            
            return age
        except ValueError:
            return "WRONG"
        
if __name__ == "__main__":
    birth_date_input = input()
    age_calculator = Agecalculate(birth_date_input)
    result = age_calculator.calculate_age()
    print(result)    