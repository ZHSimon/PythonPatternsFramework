from thraxisgamespatterns.factories.abstract_factory import TGAbstractFactory


class TGHandlerMapFactory(TGAbstractFactory):
    def create(self, options=None):
        return {}
