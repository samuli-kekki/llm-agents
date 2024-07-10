"""
MIT License

Copyright (c) 2024 Samuli Kekki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import openai
from typing import Optional
from agent_types import LLM, Message, LLMInput

class ChatGPT(LLM):
    """A wrapper for ChatGPT SDK.
    Helps with sending a list of messages to ChatGPT
    and handling the response."""

    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise KeyError("OPENAI_API_KEY environment variable not found")
        self.client = openai.OpenAI(api_key=api_key)

    def predict(self, input: LLMInput) -> Optional[Message]:
        """Call ChatGPT API with input to get a response.
        
        Args:
            input (LLMInput): Payload to send to ChatGPT API,
                Consists of system prompt and a list of messages.
        
        Returns:
            Optional[Message]: Response from ChatGPT as Message,
                or None, if ChatGPT decided to not return a response
                based on the system prompt."""

        try:
            messages_dict = [message._asdict() for message in input.messages]

            # We can insert the system prompt as the first message for ChatGPT
            system_message = {
                "role": "system",
                "content": input.system
            }

            messages_dict.insert(0, system_message)

            response = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=1024,
                messages=messages_dict
            )

            if not response:
                return None

            if not isinstance(response.choices, list):
                return None

            if len(response.choices) == 0:
                return None

            message = response.choices[0].message
            role = message.role

            if role != "assistant":
                print(f"Warning: response role is not assistant: {role}")
            
            content = message.content
            if "empty string" in content:
                return None

            return Message(role, content)
        except Exception as err:
            print(f"Exception when calling ChatGPT API: {err}")
        return None
