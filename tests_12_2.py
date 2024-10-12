import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', speed=10)
        self.andrey = Runner('Андрей', speed=9)
        self.nick = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{{{k}: {v}}}')

    def test_tournament_with_usain_and_nick(self):
        participants = [self.usain, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        expected_last_finisher = self.nick
        actual_last_finisher = results[max(results)]
        self.assertTrue(expected_last_finisher == actual_last_finisher)
        self.all_results['usain_vs_nick'] = results

    def test_tournament_with_andrey_and_nick(self):
        participants = [self.andrey, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        expected_last_finisher = self.nick
        actual_last_finisher = results[max(results)]
        self.assertTrue(expected_last_finisher == actual_last_finisher)
        self.all_results['andrey_vs_nick'] = results

    def test_tournament_with_usain_andrey_and_nick(self):
        participants = [self.usain, self.andrey, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        expected_last_finisher = self.nick
        actual_last_finisher = results[max(results)]
        self.assertTrue(expected_last_finisher == actual_last_finisher)
        self.all_results['usain_andrey_vs_nick'] = results

if __name__ == '__main__':
    unittest.main()