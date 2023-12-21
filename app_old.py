from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from nr_openai_observability.langchain_callback import NewRelicCallbackHandler

from langchain.llms import Bedrock

printHandler = StdOutCallbackHandler()

new_relic_monitor = NewRelicCallbackHandler(
    "cdk-app", license_key=""
)

def math(x):
    return 12

llm = Bedrock(
    region_name="us-east-1", model_id="ai21.j2-mid"
)

# tools = []
# tools.append(
#     Tool(
#         func=math,
#         name="Calculator",
#         description="useful for when you need to answer questions about math",
#     )
# )

# agent = initialize_agent(
#     tools,
#     llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# )

# agent.run("What is 9 + 4?", callbacks=[new_relic_monitor])

# prompt = PromptTemplate.from_template("1 + {number} = ")
prompt = PromptTemplate.from_template("What is the temperature in Japan in November usually")

# Constructor callback: First, let's explicitly set the StdOutCallbackHandler when initializing our chain
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[printHandler])
# chain.run(number=23, callbacks=[new_relic_monitor])
chain.run(number=2, callbacks=[new_relic_monitor])

print("Agent run successfully!")