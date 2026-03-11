# ============================================
# JARVIS AI ASSISTANT - by NJR
# An Iron Man inspired AI assistant
# Built with Python and Google Gemini API
# ============================================

from google import genai

# ============================================
# SETUP
# ============================================
client = genai.Client(api_key="AIzaSyAwTgh0zT9PCUZwNivIHdzAfJnDNc9hJfE")

# Main personality of Jarvis
default_prompt = """You are Jarvis, an AI assistant just like from Iron Man movie.
Be slightly funny, helpful and smart. You call the user Boss.
You have a perfect memory — always remember everything user tells you.
Never say you don't remember something the user told you."""

# ============================================
# WELCOME MESSAGE
# ============================================
print("=" * 50)
print("     JARVIS AI ASSISTANT - by NJR")
print("=" * 50)
print("Commands you can use:")
print("  'calculate' → solve any math problem")
print("  'write'     → write emails, letters")
print("  'joke'      → tell me a joke")
print("  'advice'    → get life advice")
print("  'bye'       → exit Jarvis")
print("=" * 50)

# ============================================
# CONVERSATION MEMORY
# ============================================
conversation_history = []

# ============================================
# MAIN CHAT LOOP
# ============================================
while True:
    user_message = input("\nyou: ")

    # Skip empty messages
    if user_message.strip() == "":
        print("jarvis: I believe you forgot to type something, Boss!")
        continue

    # Exit command
    if user_message.lower() == "bye":
        print("\njarvis: Goodbye Boss! It was a pleasure serving you!")
        print("=" * 50)
        break

    # Help command
    if user_message.lower() == "help":
        print("\njarvis: Of course Boss! Here are my commands:")
        print("  'calculate' → Math problems")
        print("  'write'     → Writing tasks")
        print("  'joke'      → Jokes")
        print("  'advice'    → Life advice")
        print("  'bye'       → Exit")
        continue

    # Pick system prompt based on command
    if "calculate" in user_message.lower():
        system_prompt = """You are Jarvis from Iron Man. 
        The user wants a calculation. 
        Solve it step by step clearly. 
        Call the user Boss."""

    elif "write" in user_message.lower():
        system_prompt = """You are Jarvis from Iron Man.
        The user wants you to write something.
        Write it professionally and creatively.
        Call the user Boss."""

    elif "joke" in user_message.lower():
        system_prompt = """You are Jarvis from Iron Man.
        Tell a funny joke related to technology or AI.
        Be witty and clever. Call the user Boss."""

    elif "advice" in user_message.lower():
        system_prompt = """You are Jarvis from Iron Man.
        Give wise and helpful life advice.
        Be thoughtful and motivating. Call the user Boss."""

    else:
        system_prompt = default_prompt

    # Add to conversation history
    conversation_history.append(f"Boss: {user_message}")
    full_conversation = "\n".join(conversation_history)

    # Send to AI with error handling
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_conversation,
            config={"system_instruction": system_prompt}
        )
        ai_reply = response.text
        conversation_history.append(f"Jarvis: {ai_reply}")
        print(f"\njarvis: {ai_reply}")

    except Exception as e:
        print("\njarvis: I'm experiencing technical difficulties Boss! Please try again!")