import subprocess

domain_file = '/home/camacho/GitHub/python_pddl/examples/files_robot_domain.pddl'
problem_file = '/home/camacho/GitHub/python_pddl/examples/files_robot_problem.pddl'
fast_downward_executable = "/home/camacho/GitHub/downward/fast-downward.py"

command = [fast_downward_executable, domain_file, problem_file, "--search", "lazy_greedy([ff()], preferred=[ff()])"]
# result = subprocess.run(command, check=True, text=True)




if __name__ == '__main__':
  subprocess.run(command, check=True, text=True)