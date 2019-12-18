class Dog:
    """
    Takes no parameters
    Creates an instance of a Dog with name and next properties
    """
    def __init__(self):
        self.name = 'Ima dog'
        self.next = None

class Cat:
    def __init__(self):
        self.name = 'Ima cat'
        self.next =  None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, animal):
        if animal.lower() == 'dog':
            new_dog = Dog()
            if self.end:
                self.end.next = new_dog
                self.end = new_dog
            elif self.front:
                self.front.next = new_dog
                self.end = new_dog
            else:
                self.front = new_dog

        if animal.lower() == 'cat':
            new_cat = Cat()
            if self.end:
                self.end.next = new_cat
                self.end = new_cat
            elif self.front:
                self.front.next = new_cat
                self.end = new_cat
            else:
                self.front = new_cat

        else:
            return 'Dogs and Cats only please.'

    def dequeue(self, pref=''):
        new_queue, front, looking, first = AnimalShelter(), self.front, True, None
        if self.front:
            self.front = front.next
        while front:
            if pref.lower() == 'cat' and looking:
                if isinstance(front, Cat):
                    first = front
                    looking = False
                else:
                    new_queue.enqueue('dog')
                    front = self.front

            if pref.lower() == 'dog'and looking:
                if isinstance(front, Dog):
                    first = front
                    looking = False
                else:
                    new_queue.enqueue('cat')
                    front = self.front

            else:
                return front
        return first                  