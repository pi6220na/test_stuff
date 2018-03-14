class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)



#myIndent = Indenter()

#myIndent.print('hello')
#myIndent.print('hello')
#myIndent.print('hello')


with Indenter() as indent:
    indent.print("level one")
    with indent:
        indent.print("level two")
