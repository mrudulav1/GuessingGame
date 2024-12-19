import random
from django.shortcuts import render
from django.http import HttpResponse

def guess_number(request):
    # Initialize the session variable for the random number
    if 'number_to_guess' not in request.session:
        request.session['number_to_guess'] = random.randint(1, 100)
        request.session['attempts'] = 0

    # Get the number to guess and the number of attempts
    number_to_guess = request.session['number_to_guess']
    attempts = request.session['attempts']

    # Handle the guess from the user
    if request.method == "POST":
        try:
            guess = int(request.POST['guess'])
            attempts += 1
            request.session['attempts'] = attempts
            if guess < number_to_guess:
                message = "Too low! Try again."
            elif guess > number_to_guess:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed it in {attempts} attempts!"
                # Reset the game if the user guessed correctly
                del request.session['number_to_guess']
                del request.session['attempts']
        except ValueError:
            message = "Please enter a valid number."

    else:
        message = "Guess a number between 1 and 100."

    return render(request, 'guess_number.html', {'message': message, 'attempts': attempts})

