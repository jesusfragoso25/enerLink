from ollama import chat


class OllamaException(Exception):
    pass


class OllamaService:

    MODEL = "qwen2.5:3b"

    @classmethod
    def ask(cls, prompt: str) -> str:

        try:

            response = chat(

                model=cls.MODEL,

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

                options={

                    "temperature": 0,

                    "top_p": 0.1,

                    "top_k": 20,

                    "repeat_penalty": 1.05,

                    "num_predict": 512,

                },

            )

            return response.message.content.strip()

        except Exception as e:

            raise OllamaException(
                f"No fue posible comunicarse con Ollama: {e}"
            )