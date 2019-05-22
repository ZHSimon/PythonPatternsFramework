from thraxisgamespatterns.patterns.abstract_executable import TGAbstractExecutable


class TGDoNothingExecutable(TGAbstractExecutable):

    def execute(self):
        # Do nothing.
        pass


DEFAULT = TGDoNothingExecutable()
