import os


from groq import Groq

def get_state_info(states):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    prompt = f"Me dê 3 curiosidades sobre os seguintes estados: {states}."

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[

            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
