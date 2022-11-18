from brain_games import cli


def run(game):
    cli.welcome()
    name = cli.get_name()
    cli.greet(name)
    print(game.DESCRIPTION)
    for _ in range(3):
        q, a = game.generate_qa_pair()
        print('Question: {}'.format(q))
        answer = cli.get_answer()
        if (answer == a):
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{a}'")
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
