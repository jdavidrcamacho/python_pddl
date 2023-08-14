import subprocess

domain_file = '/home/camacho/GitHub/python_pddl/examples/prob_domain.pddl'
problem_file = '/home/camacho/GitHub/python_pddl/examples/prob_problem.pddl'
fast_downward_executable = "/home/camacho/GitHub/downward/fast-downward.py"

command = [fast_downward_executable, domain_file, problem_file, "--search", "lazy_greedy([ff()], preferred=[ff()])"]
result = subprocess.run(command, check=True, text=True)


#cmd = [fast_downward_executable, "--search", "lama-first", domain_file, problem_file]
#retcode = subprocess.call(cmd, shell=True, check=True, capture_output=True, text=True)
#print(retcode)