import google.generativeai as genai

def main():
    api_key = "YOUR_API_KEY"
    genai_client = genai.GenerativeAI(api_key)
    prompt = "Write a story about a character who discovers a hidden world."
    generated_text = genai_client.generate_text(prompt)
    print(generated_text)

if __name__ == "__main__":
    main()