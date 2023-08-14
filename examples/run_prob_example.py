import pddlpy


domprob = pddlpy.DomainProblem('prob_domain.pddl', 'prob_problem.pddl')


print('initial state:', domprob.initialstate())
print('operators:', list(domprob.operators()))
