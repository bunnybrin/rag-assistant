import os

import inspect
from dotenv import load_dotenv
from llama_cloud.client import LlamaCloud
from llama_cloud_services import LlamaCloudIndex
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import CitationQueryEngine, RetrieverQueryEngine
from llama_index.core import Settings, get_response_synthesizer, PromptTemplate
from llama_index.core.response_synthesizers import ResponseMode

from src.config.prompts import text_qa_template, refine_template, summary_template, simple_template

load_dotenv()

llama_cloud_api_key = os.environ["LLAMA_CLOUD_API_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

client = LlamaCloud(token=llama_cloud_api_key)
pipeline_id = '47f1daa6-4e58-4021-a5aa-64245eedc67a'

Settings.llm = OpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=openai_api_key,
)





index = LlamaCloudIndex(
    name="appalling-bass-2025-11-11",
    project_name="Default",
    organization_id="6a4701a8-5d2f-4a92-a8fa-8f8089062598",
    api_key=llama_cloud_api_key,
)

synth = get_response_synthesizer(
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template,
    refine_template=refine_template,
    summary_template=summary_template,
    simple_template=simple_template
)

retriever = index.as_retriever(similarity_top_k=30, rerank_top_n=6, enable_reranking=True,  retrieval_mode='chunks')


# nodes = retriever.retrieve('з яких джерел ти можеш надати інформацію?')
query_engine = RetrieverQueryEngine.from_args(
    retriever=retriever,
    # node_postprocessors=[reranker],
    response_synthesizer=synth,
)


response = query_engine.query("з яких джерел ти можеш надати інформацію?")
# response = query_engine.query("С каких источников ти можеш надать информацию?")
print("Відповідь з цитатами:")
print(response)

response2 = query_engine.query("Роскажи про документ наведений в 2 пункті")
print(response2)



# User Question → Retriever → QueryEngine → Prompt Builder → LLM → Synthesizer → Output