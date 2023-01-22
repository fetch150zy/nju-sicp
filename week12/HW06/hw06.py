""" Homework 6: OOP and Inheritance"""

#####################
# Required Problems #
#####################

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    # !
    def __init__(self, product, price) -> None:
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self) -> str:
        if self.stock <= 0:
            return 'Machine is out of stock.'
        if self.balance >= self.price:
            self.stock -= 1
            self.balance -= self.price
            if self.balance > 0:
                tmp = 'Here is your {} and ${} change.'.format(self.product, self.balance)
                self.balance = 0
                return tmp
            else:
                return 'Here is your {}.'.format(self.product)
        else:
            return 'You must add ${} more funds.'.format(self.price - self.balance)

    def add_funds(self, balance) -> str:
        if self.stock <= 0:
            return 'Machine is out of stock. Here is your ${}.'.format(balance)
        self.balance += balance
        return 'Current balance: ${}'.format(self.balance)

    def restock(self, stock) -> str:
        self.stock += stock
        return 'Current {} stock: {}'.format(self.product, self.stock)


class Pet:
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)


class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        # !
        super(Cat, self).__init__(name, owner)
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        """
        "*** YOUR CODE HERE ***"
        # !
        print('{} says meow!'.format(self.name))

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        "*** YOUR CODE HERE ***"
        # !
        if not self.is_alive:
            print('{} has no more lives to lose.'.format(self.name))
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False


class NoisyCat(Cat): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? If not, feel free to remove it.
        "*** YOUR CODE HERE ***"
        # !
        super(NoisyCat, self).__init__(name, owner, lives)
    
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        "*** YOUR CODE HERE ***"
        # !
        print('{} says meow!'.format(self.name))
        print('{} says meow!'.format(self.name))


##########################
# Just for fun Questions #
##########################

class Fib:
    """A Fibonacci number.

    >>> start = Fib()
    >>> start.value
    0
    >>> start.next().value
    1
    >>> start.next().next().value
    1
    >>> start.next().next().next().value
    2
    >>> start.next().next().next().next().value
    3
    >>> start.next().next().next().next().next().value
    5
    >>> start.next().next().next().next().next().next().value
    8
    >>> start.value # Ensure start isn't changed
    0
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        # !
        if self.value != 0:
            tmp = Fib(self.value + self.previous)
        else:
            tmp = Fib(1)
        tmp.previous = self.value
        return tmp
