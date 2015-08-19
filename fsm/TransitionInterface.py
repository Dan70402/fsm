class TransitionInterface(object):

    def transition(self, input):
        """
        Logic to apply before changing the state of a step.  Return True if successful and
        False if not

        :param input:
        :return: <bool>
        """
        raise NotImplementedError("transition() not implemented")