from graphviz import Digraph

dot = Digraph(comment='The TreeSong Table')

dot.node('A', 'Dot A')
dot.node('B', 'Dot B')
dot.node('C', 'Dot C')
dot.node('D', 'Dot D')
dot.node('E', 'Dot E')
dot.node('F', 'Dot F')

dot.edges(['AB', 'DC', 'AD', 'BE', 'EF'])
dot.view()

print(dot.source)

dot.render('test-output/TreeSong.gv', view=True)