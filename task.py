list_of_branches = []


class Branch:

    def __init__(self, name, text):
        self.name = name
        self.text = text
        list_of_branches.append(self)

    @staticmethod
    def print_text():
        for i in range(len(list_of_branches)):
            print(list_of_branches[i].text)


branch1_Tsoy = Branch('first', 'Кружась, сияет вихрь реальности и снов,')
branch2_Tsoy = Branch('second', 'Вселенная живёт, творя и вновь губя.')
branch3_Tsoy = Branch('third', 'У космоса есть много голосов,')
branch4_Tsoy = Branch('fourth', 'Он полон тайн. И он зовёт тебя.')
branch1_Cure = Branch('first', 'Spinning, shining whirlwind of reality and dreams,')
branch2_Cure = Branch('second', 'The universe lives, creating and destroying again.')
branch3_Cure = Branch('third', 'The cosmos has many voices')
branch4_Cure = Branch('fourth', 'He is full of secrets. And he calls you.')

Branch.print_text()