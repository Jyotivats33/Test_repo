import openai


def loginOpenAI(text):
    prompt = f"""
       Extract validation rules from the following text and return them in JSON format:
       """
    prompt+= text
    client = openai.OpenAI(api_key= )


    response = client.embeddings.create(
    model="text-embedding-ada-002",
    input=prompt
    )

    return response.data[0].embedding