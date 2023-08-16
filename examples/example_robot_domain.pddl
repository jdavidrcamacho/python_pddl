(define (domain robot-movement)
    (:requirements :strips :typing)
    
    (:types room object)
    
    (:predicates
        (at ?obj - object ?room - room)
    )
    
    (:action move
        :parameters (?obj - object ?from - room ?to - room)
        :precondition (and
            (at ?obj ?from)
        )
        :effect (and
            (at ?obj ?to)
            (not (at ?obj ?from))
        )
    )
)
