import random


def get_words_from_file(path):
    '''Получает все слова из файла списком'''

    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.read()
        words = lines.splitlines()

    return words


def shuffle_word(word):
    '''Перемешивает буквы в словаре'''
    word_as_list = list(word)
    random.shuffle(word_as_list)
    return ''.join(word_as_list)


def save_player_score(player_name, player_score):

    path = 'history.txt'
    with open(path, "a", encoding='utf-8') as fp:
        fp.write(f'{player_name} {player_score}\n')


def get_statistics_from_file(path):

    path = 'history.txt'
    scores = []
    with open(path, 'r', encoding='utf-8') as fp:
        for line in fp:
            score = line.strip().split(" ")[-1]
            scores.append((int(score)))

    max_score = max(scores)
    games_played = len(scores)

    return {'max_score': max_score, 'games_played': games_played}
