from langchain_openai import ChatOpenAI
import os
from langchain_community.document_loaders  import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable

model =ChatOpenAI(model="gpt-4", openai_api_key=my_api_key)


# loading the yt viode transcript
video_id = "_3ezSpJw2E8"
loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=TGVLmr194DI&list=PLZPZq0r_RZOOj_NOZYq_R2PECIMglLemc&index=2")
transcript = loader.load()
transcript = transcript[0].page_content

print(type(transcript))

# splitting it into chunks to pass to the model
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # Max characters per chunk
    chunk_overlap=100,    # Overlap to preserve context
    separators=[
        "\n\n",           # Prefer splitting by paragraphs
        "\n",             # Then by lines
        ".",              # Then by sentences
        " ",              # Then by words
        ""                # Fallback: split by characters
    ]
)

chunks_transcript = splitter.split_text(transcript)
# now I need to make vector embedding for the chunks
