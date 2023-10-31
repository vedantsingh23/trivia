import random

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class TriviaGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_game(self):
        print("Trivia Category: Cars")
        print("Rules: Every question answered correctly is one point, and incorrect answers are zero points.")
        random.shuffle(self.questions)
        
        for question in self.questions:
            print("\nQuestion: ", question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            
            user_answer = int(input("Enter the number of your answer: "))
            if question.check_answer(user_answer - 1):
                print("Correct! You earned 1 point.")
                self.score += 1
            else:
                print("Incorrect. The correct answer is:", question.options[question.correct_answer])

        print(f"Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    questions = [
        Question("What is the fastest naturally aspirated car?", ['Mclaren F1', 'Bugatti Chiron', 'Koenigsegg Agera RS', 'Lamborghini Huracan'], 0),
        Question("Where did Ferrari originate from?", ['USA', 'France', 'Italy', 'Germany'], 2),
        Question("What car brand made the Huracan Model", ['Mclaren', 'Ferrari', 'Ford', 'Lamborghini'], 3),
        Question("What is the quickest accelerating car?", ['Dodge Demon 170', 'Rimac Nevera', 'Ferrari SF90', 'BMW M5CS'], 0),
        Question("What was the first hybrid car made by Toyota?", ['Corolla', 'Camry', 'Supra', 'Prius'], 3),
        Question("What is the most expensive car ever sold?", ['Ferrari 250 GTO', 'Mercedes 300SLR', 'Bugatti Chiron', 'Mclaren F1'], 1),
        Question("What brand made the skyline cars?" , ['Ferrari','Toyota', 'Nissan', 'BMW'], 2),
        Question('What engine do Corvettes have?',['V8','V12','V6','I4'],0),
        Question('What type of car has 2 doors?',['SUV','Sedan', 'Coupe', 'Van'],2),
        Question('What company is famously known for utilizing the rotary engine?',['Toyota', 'Lamborghini', 'Audi', 'Mazda'],3),
        Question('What car has the same engine as a Lamborghini Huracan',['Audi R8', 'Lamborghini Aventador', 'Ferrari Roma', 'Mclaren 720s'],0),
        Question('Which one of these cars make the most power?',['Koenigsegg Jesko', 'Bugatti Chiron Super Sport', 'Mclaren Speedtail', 'Henessey Venom F5'], 3),
        Question('Which one of these cars is considered one of the best sounding cars ever?', ['BMW M5', 'Lexus LFA', 'Porsche 911', 'Toyota Supra'],1),
        Question('Audi Won Le Mans consistently implementing the usage of: ',['Turbochargers', 'Superchargers', 'Hybrid Technology', 'Diesel Technology'], 3),
        Question('What is the biggest car event in the world?',['Concours Delegance', 'Cars and Coffee', 'Monterey Car Week', 'Nascar Championships'], 2),
        Question('Which one of these cars use both a turbo and a supercharger?',['Lancia Delta S4', 'Audi Quattro S1', 'Ford RS200','Mercedes 300SL Gullwing'], 0),
        Question('What was the first car to go 200mph?',['Ferrari F40', 'Lamborghini countach', 'Bmw Nazca C12', 'Dodge Charger Daytona'], 3),
        Question('What was the most dominant F1 team?',['Porsche', 'Ferrari', 'Alfa Romeo', 'Mercedes'],1),
        Question('What car brand has AMG as their performance engines',['Mercedes', 'Alfa Romeo', 'BMW', 'Audi'], 0),
        Question('What car brand has M as their performance engines',['Mercedes', 'Alfa Romeo', 'BMW', 'Audi'], 2),
        Question('What car brand has RS as their performance engines',['Mercedes', 'Alfa Romeo', 'BMW', 'Audi'], 3),
        Question('Which race car is known as the Widow Maker',['Porsche GT3RS', 'Porsche 917', 'Mercedes AMG GTR', 'Nissan GTR'], 1),
        Question('What car brand uses VTEC technology?', ['Honda','Mazda', 'Ford', 'Chevrolet'], 0)

    ]

    game = TriviaGame(questions)
    game.run_game()