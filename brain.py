import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_hassan_response(user_query):
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY not found in .env file!"

    try:
        with open("./data/hassan_facts.txt", "r") as f:
            context_text = f.read()
    except FileNotFoundError:
        return "Error: I can't find 'data/hassan_facts.txt'. Please check your folders!"

    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

    prompt = f"""
    You are an expert guide for Hassan, Karnataka.
    Use the following information to answer the question:
    
    {context_text}
    
    Question: {user_query}
    """

    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    print("🚀 Hassan AI is starting up...")
    try:
        result = get_hassan_response("Tell me about Shettihalli Church")
        print("\n✅ AI RESPONSE:")
        print(result)
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")