class ConditionInterface(object):

    def condition(self, input):
        """
        Evaluates an input and returns True|False if the machine should
        proceed with the transition

        :param input:
        :return <boolean>:
        """
        raise NotImplementedError("condition() not implemented")