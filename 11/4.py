class PatternGenerator:
    def __init__(self, n):
        self.n = n

    def generate_pattern(self):
        if self.n % 2 == 1:
            pattern = [['*' for _ in range(self.n)] for _ in range(self.n)]
            return pattern
        else:
            return f"{self.n} عددی زوج است."

n1 = 3
pattern_generator = PatternGenerator(n1)
result = pattern_generator.generate_pattern()

if isinstance(result, list):
    for row in result:
        print(' '.join(row))
else:
    print(result)

n2 = 4
pattern_generator = PatternGenerator(n2)
result = pattern_generator.generate_pattern()
print(result)
