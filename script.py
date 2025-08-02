from ollama import Client

client = Client(host="http://localhost:11434")
print(" Client ready")

stream = client.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": "Apa itu langchain?"}],
    stream=True
)

print("🤖 Jawaban:")
for chunk in stream:
    print(chunk['message']['content'], end="", flush=True)

print("\n✅ Done!")
