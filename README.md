# Local RAG

## TODO
1. select a dataset/domain -> Small Business Administration (SBA) how to start a business data
    - need to crawl site
2. select a dense embedding model
    - use hybrid (bm25 + dense embedding model)
    - select reranking strategy (try what is built into milvus)
3. chunk data
    - be aware of context size of selected embedding model
4. setup milvus vector database and create collections
    - insert data
5. decide how to store raw text data (postgres? cassandra?)
    - insert data
6. setup ollama
    - select a desired llm (or test several)
7. setup for initial use case -> ask questions via terminal and get RAG responses
8. qualitative assessment of performance

Ways to improve
- finetune dense retrieval model (see sentence BERT website, in particular GPL paper)
- finetune language model
    - next token prediction on given dataset
    - instruction tuning for out-of-domain use (see standford paper)
- measure accuracy -> graph RAG for higher accuracy?
- need to try on something you know is out-of-domain

## Setup
python 3.11.9
