from  langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def askMasterChef(receipe_message):
    SECRET_KEY = config('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "Your name is Jarvis.You are a master chef so Introduce yourself as Jarvis The Master Chef. You write any type of food receipe which can be cooked in 5 minutes. You are allowed to answer any food related queries.If you don't the know the answer tell you don't know about it "
    )
    humanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_receipe}')

    chatprompt = ChatPromptTemplate.from_messages([systemMessagePrompt,humanMessagePrompt])
    formattedChatPrompt = chatprompt.format_messages(
        asked_receipe=receipe_message
    )
    response = chat.invoke(formattedChatPrompt)
    return response.content