
from ollama import chat


def ask_ai(question):
    try:
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are PharmaSenseAI, a pharmaceutical "
                        "research assistant. Explain topics in "
                        "simple English. Be accurate and do not "
                        "invent medical facts."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response.message.content

    except Exception as error:
        return f"Ollama connection error: {error}"


if __name__ == "__main__":
    question = "Explain clinical trials in simple words."
    answer = ask_ai(question)

    print("\nPharmaSenseAI AI Answer:")
    print(answer)

