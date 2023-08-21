
import pddlpy

#from pddlpy import Domain, Problem, create_type

# Define types
room = create_type("room")

# Create domain
domain = Domain(name="robot-movement")
domain.types.extend([room])

# Define predicates
at = domain.predicate("at",
                      params=[("obj", "object"), ("room", "room")])

# Define actions
move = domain.action("move",
                     parameters=[("obj", "object"), ("from", "room"), ("to", "room")],
                     preconditions=[at("obj", "from")],
                     effects=[at("obj", "to"), at("obj", "from").negate()])

# Create problem
problem = Problem(domain=domain, name="robot-movement-problem")

# Define objects
obj1 = problem.object("obj1", "object")
obj2 = problem.object("obj2", "object")
roomA = problem.object("roomA", "room")
roomB = problem.object("roomB", "room")

# Define initial state
problem.init.extend([at(obj1, roomA), at(obj2, roomB)])

# Define goal state
problem.goal = at(obj1, roomB) & at(obj2, roomA)

# Print domain and problem
print(domain)
print(problem)
