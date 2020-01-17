BuiltinImporter

print('Welcome to Rock Paper Scissors!')

choices = ['rock', 'paper', 'scissor']
score = 0
playing = True

outcomes = {
    'rock': {
        'rock': 'tie',
        'paper': 'lose',
        'scissor': 'win'
    },
    'paper': {
        'rock': 'win',
        'paper': 'tie',
        'scissor': lose
    },
    'scissor': {
        'rock': 'lose',
        'paper': 'win',
        'scissor': 'tie'
    }
}

while playing == True :
    # players picking what they want 
    player_choice = raw_input('Choose rock, paper, or scissor: ')
    comp_choice = random.choice(choices)
    
    if outcomes[player_choice] [comp_choice] == 'win':
        score += 1
        print('You Win!', score )
    elif outcomes[player_choice] [comp_choice] == 'tie':
        print('You tied!', score )
    elif outcomes[player_choice] [comp_choice] == 'lose':
        print('You lose sucka!')
        playing = False 
        print('Your score: ', score )
        
        

