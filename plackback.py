import pickle
from individual import INDIVIDUAL

f = open('robot copy.p', 'rb')
best = pickle.load(f)
f.close()

best.Evaluate(False)
print(best.fitness)
# for i in best:
#     best[i].Start_Evaluation(False)
#     print(best[i].fitness)
