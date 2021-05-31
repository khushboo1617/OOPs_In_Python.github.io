class Boy:
    def __init__(self):
        self.name = 'maan'
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


b1 = Boy()
b2 = Boy()

print(b1.name)
print()

# b2.age=50

if b1.compare(b2):
    print('same')
else:
    print('not same')

