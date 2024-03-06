from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All
import paths

def text_to_EntityPrice(question:str):
    template = """text :  - {question}
              task : Please generate a list of entities and their corresponding prices. each should be in seperate list and output that lists, for example [cab, fries, new phone][5,7,1000]"""

    prompt = PromptTemplate.from_template(
        template = template)

    llm = GPT4All(model=paths.MODEL, verbose=True)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    result = llm_chain.run(question)
    entities = eval(result.strip("\n").split('\n')[0].split('=')[1])
    prices = eval(result.strip("\n").split('\n')[1].split('=')[1])
    return entities, prices