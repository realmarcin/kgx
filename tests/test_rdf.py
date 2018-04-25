from kgx import ObanRdfTransformer, PandasTransformer, GraphMLTransformer, JsonTransformer

def test_load():
    """
    load tests
    """
    t = ObanRdfTransformer()
    t.parse("tests/resources/monarch/biogrid_test.ttl")
    t.report()
    w1 = PandasTransformer(t)
    w1.save('target/bgcopy.csv', type='e')
    w2 = GraphMLTransformer(t)
    w2.save("target/x1n.graphml")
    w3 = JsonTransformer(t)
    w3.save("target/x1n.json")
