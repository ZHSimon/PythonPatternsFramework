from thraxisgamespatterns.eventhandling.abstract_reaction import TGAbstractReaction


class TGDummyReaction(TGAbstractReaction):
    def react_to(self, subject):
        return  # Do nothing.
