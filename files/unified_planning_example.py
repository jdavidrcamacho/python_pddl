from unified_planning.shortcuts import *

Location = UserType('Location')


from unified_planning.io import PDDLReader
# Reader used with both domain and problem file
reader = PDDLReader()

# domain_filename = ... # path of the PDDL domain file
domain_filename = 'prob_domain.pddl'

# problem_filename = ... # path of the PDDL problem file
problem_filename =  'prob_problem.pddl'

problem = reader.parse_problem(domain_filename, problem_filename)


with OneshotPlanner() as planner:
    result = planner.solve(problem)
    if result.status == up.engines.PlanGenerationResultStatus.SOLVED_SATISFICING:
        print("Plan returned: %s" % result.plan)
    else:
        print("No plan found.")

# print(planner)


plan = result.plan
with PlanValidator(problem_kind=problem.kind, plan_kind=plan.kind) as validator:
    if validator.validate(problem, plan):
        print('The plan is valid')
    else:
        print('The plan is invalid')

# print(problem, plan)