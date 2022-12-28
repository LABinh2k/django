from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
es.info().body

import pandas as pd

df = (
    pd.read_csv("wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)

mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            "ethnicity": {"type": "text", "analyzer": "standard"},
            "director": {"type": "text", "analyzer": "standard"},
            "cast": {"type": "text", "analyzer": "standard"},
            "genre": {"type": "text", "analyzer": "standard"},
            "plot": {"type": "text", "analyzer": "english"},
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
    }
}

es.indices.create(index="movies", mappings=mappings)

for i, row in df.iterrows():
    doc = {
        "title": row["Title"],
        "ethnicity": row["Origin/Ethnicity"],
        "director": row["Director"],
        "cast": row["Cast"],
        "genre": row["Genre"],
        "plot": row["Plot"],
        "year": row["Release Year"],
        "wiki_page": row["Wiki Page"]
    }
            
    es.index(index="movies", id=i, document=doc)
    
    
resp = es.search(
    index="movies",
    body={
        "query": {
            "bool": {
                "must": {
                    "match_phrase": {
                        "cast": "kok",
                    }
                },
                "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},
            },
        },            
    }
)
resp