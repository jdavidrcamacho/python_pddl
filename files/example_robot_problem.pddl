(define (problem robot-movement-problem)
    (:domain robot-movement)
    
    (:objects obj1 obj2 - object
              roomA roomB - room)
              
    (:init
        (at obj1 roomA)
        (at obj2 roomB)
    )
    
    (:goal (and
        (at obj1 roomB)
        (at obj2 roomA)
    ))
)
