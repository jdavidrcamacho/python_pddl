(define (domain robot-domain)
    (:requirements :strips)
    (:types location block)
    (:predicates
        (at ?b - block ?loc - location)
        (empty-handed)
    )
    (:action pickup
        :parameters (?b - block ?loc - location)
        :precondition (and (at ?b ?loc) (empty-handed))
        :effect (and (not (at ?b ?loc)) (not (empty-handed)))
    )
    (:action putdown
        :parameters (?b - block ?loc - location)
        :precondition (and (not (at ?b ?loc)) (not (empty-handed)))
        :effect (and (at ?b ?loc) (empty-handed))
    )
    (:action move
        :parameters (?b - block ?from - location ?to - location)
        :precondition (and (at ?b ?from) (not (empty-handed)))
        :effect (and (at ?b ?to) (not (at ?b ?from)))
    )
)
