from openai import OpenAI

# שימי כאן את ה-API KEY שלך
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# קוראים את ה-prompt
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

messages = [
    {"role": "system", "content": prompt}
]

print("Simulation started. Type exit to stop\n")

while True:

    user_input = input("Agent: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    print("\nCustomer:", reply, "\n")

    messages.append({"role": "assistant", "content": reply})