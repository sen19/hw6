from utils import *
from config import WORDS_PATH, HISTORY_PATH


def main():
    user_score = 0

    print('Введите ваше имя')
    user_name = input()

    words = get_words_from_file(WORDS_PATH)

    for word in words:
        word_shuffled = shuffle_word(word)
        print(f'Угадай слово: {word_shuffled}')

        user_input = input()

        if user_input == word:
            user_score += 10
            print('Верно! Вы получаете 10 очков')
        else:
            print(f'Неверно! Верный ответ - {word}')

    save_player_score(user_name, user_score)

    stats = get_statistics_from_file(HISTORY_PATH)

    print(f"Всего игр сыграно: {stats.get('games_played')}")
    print(f"Максимальный рекорд: {stats.get('max_score')}")


main()
