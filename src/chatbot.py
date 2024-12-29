import getpass
import os

if not os.environ.get("OPEN_API_KEY"):
    os.environ["OPEN_API_KEY"] = getpass.getpass("Enter your API key for OpenAI: ")

from langchain_community.chat_models import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

from langchain_core.messages import HumanMessage

model.invoke([HumanMessage(content="Hi! I'm Bob")])
