from eddy import logger

class StateMachine(object):
    """
    A table driven state machine
    """

    def __init__(self, trans_table):
        """
        TransTable holds all the machine state logic.  It is in the format:

        trans_table = [
            {(CURRENT_STATE, TRIGGER) : (CONDITION, TRANSITION, NEXT_STATE)}},
            {(CURRECT_STATE, ANOTHERTRIGGER) : (CONDITION, TRANSITION, NEXT_STATE)},
            ...
        ]

        For matching states the order is processed in the order they are declared.  A condition will return True
        if the step should proceed to execute the transition.  The transition will either return True | False.  False
        indicated the transition failed.  If a transition returns true the NEXT_STATE is set and the machine stops
        processing the trans_table

        :param trans_table:
        :return:
        """
        self.trans_table = trans_table

    def nextStep(self, input):
        for rule in self.trans_table:
            for (state, input_type),(condition, transition, next_state) in rule.iteritems():
                if not state == input.state:
                    #The state does not match the current rule
                    continue

                if not isinstance(input, input_type):
                    #The input type does not match the current rule
                    continue

                if not condition().condition(input):
                    #The condition is not valid for the current rule
                    continue

                changed = transition().transition(input)
                if changed:
                    #transition was successful :)
                    input.state = next_state
                    return

        logger.debug("Nothing to run for input in current state")