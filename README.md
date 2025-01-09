# GPT-Engineer + GROQ and GPT-Engineer + LLAMA.CPP

- Groq: connecting it to `Groq` to have ability to use their model and enjoy fast inference speed
- Llama.cpp: To be able to use python libraries and set a server using `llama.cpp` so that we can use any `hugginface` `GGUF` models and have another termial running the `client` which is `gpte` (GPT-Engineer)


**Please read notes for more details.**

Initially tried with Google Gemini-2.0-flash-exp but it didn't work as the BASE_URL is not OpenAI compatible.
But had created a service account and downloaded the .json file credentials and have set a helper function
to update the `OPENAI_API_KEY` env var on the fly to have authorization and be able authenticate
but it doesn't work like that as it adds a `/chat/completion` at the end of the url.

