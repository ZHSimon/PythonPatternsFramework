from abc import abstractmethod, ABC


class TGAbstractQuickSorter(ABC):
    @abstractmethod
    def get_values(self):
        return []

    def sort(self, array=[]):
        if not array:
            array = self.get_values()
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for value in array:
                if value < pivot:
                    less.append(value)
                elif value == pivot:
                    equal.append(value)
                elif value > pivot:
                    greater.append(value)
            return self.sort(less) + equal + self.sort(greater)
        else:
            return self.get_values()
