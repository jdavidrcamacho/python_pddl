import subprocess
import pytest

domain_file = '/home/camacho/GitHub/python_pddl/files/prob_domain.pddl'
problem_file = '/home/camacho/GitHub/python_pddl/files/prob_problem.pddl'
fast_downward_executable = "/home/camacho/GitHub/downward/fast-downward.py"

command = [fast_downward_executable, domain_file, problem_file, "--search", "lazy_greedy([ff()], preferred=[ff()])"]
# result = subprocess.run(command, check=True, text=True)


# cmd = [fast_downward_executable, domain_file, problem_file, "--search", "lama-first"]
# retcode = subprocess.call(cmd,  check=True, capture_output=True, text=True)
# print(retcode)

def sum_ab(a: float, b: float) -> float:
    return a+b


if __name__ == '__main__':
  subprocess.run(command, check=True, text=True)