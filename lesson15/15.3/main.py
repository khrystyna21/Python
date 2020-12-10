from boss_class import Boss
from worker_class import Worker

big_boss = Boss(1, 'BIG Boss', 'Family Company')
small_boss = Boss(2, 'BIG Boss', 'Family Company')
not_a_boss = Worker(2, 'Kate NOT A BOSS ', 'Family Company', big_boss)
my_worker = Worker(1, 'John Worker ', 'Family Company', big_boss)
# my_worker = Worker(1, 'John Worker ', 'Family Company', not_a_boss)


# print(my_worker)
# print("Boss1: ", big_boss, ", Number of workers : ", len(big_boss.workers))
#
# my_worker.boss = small_boss
# #my_worker.boss = not_a_boss
# #
# print(my_worker)
# print("Boss1: ", big_boss, ", Number of workers : ", len(big_boss.workers))
# print("Boss2: ", small_boss, ", Number of workers : ", len(small_boss.workers))

class Not_worker:
    def __init__(self, name):
        self.name = name

not_worker = Not_worker('Tom')

print(len(big_boss.workers))
big_boss.workers.append(not_worker)
print(len(big_boss.workers))