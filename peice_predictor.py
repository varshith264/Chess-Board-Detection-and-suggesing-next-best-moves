
#pass the y_pred list to this finction from ML model.predict and this function returns the name of the peice in the corresponding square.
def predict(probabilities):
    target_names = ['BB', 'BK', 'BN', 'BP', 'BQ', 'BR',
                    'Empty', 'WB', 'WK', 'WN', 'WP', 'WQ', 'WR']

    peices = {'B': 'Bishop', 'K': 'King', 'N': 'Knight',
            'P': 'pawn', 'Q': 'Queen', 'R': 'Rook'}
    current_value = -1
    current_index = -1
    for i in range(len(probabilities)):
        if (probabilities[i] > current_value):
            current_index = i
            current_value = probabilities[i]
    
    name = target_names[current_index]
    if (len(name) == 5):
        return 'Empty'
    elif name[0] == 'W':
        return 'White ' + peices[name[1]]
    else:
        return 'Black ' + peices[name[1]]






     
