(define (problem block-mover)
    (:domain robot-domain)
    (:objects
        blockA - block
        blockB - block
        location1 - location
        location2 - location
    )
    (:init
        (at blockA location1)
        (at blockB location2)
        (empty-handed)
    )
    (:goal
        (and
            (at blockA location2)
            (at blockB location1)
        )
    )
)
