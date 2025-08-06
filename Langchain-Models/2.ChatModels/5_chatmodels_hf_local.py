from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "/D:huggingface_cache" # set to another directory if you want (by default it's in the C directory)

llm = HuggingFacePipeline(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("what is the capital of France?")

print(result.content)