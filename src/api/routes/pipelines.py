from fastapi import APIRouter

router = APIRouter()

import os

from dotenv import load_dotenv

load_dotenv()

from llama_cloud.client import LlamaCloud

llama_cloud_api_key = os.environ["LLAMA_CLOUD_API_KEY"]

client = LlamaCloud(token=llama_cloud_api_key)
pipeline_id = '47f1daa6-4e58-4021-a5aa-64245eedc67a'

@router.get("/pipelines")
async def get_pipelines():
    return client.pipelines.list_pipeline_documents(pipeline_id)
    # return client.pipelines.paginated_list_pipeline_documents(pipelineв_id)


@router.get("/files/{file_id}")
async def get_pipelines(file_id: str):
    return client.files.read_file_content(file_id).url
