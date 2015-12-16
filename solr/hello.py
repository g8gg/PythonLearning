from SolrClient import SolrClient

solr = SolrClient('http://localhost:8983/solr')
res = solr.query('techproducts', {
    'q': 'ipod', 'facet': True,
    'indent': True
})
print(res.get_results_count())
print(res.get_facets())
print(res.get_json())
