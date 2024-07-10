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
import anthropic
from typing import Optional
from agent_types import LLM, Message, LLMInput

class Claude(LLM):
    """A wrapper for Claude SDK.
    Helps with sending a list of messages to Claude
    and handling the response."""

    def __init__(self):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise KeyError("ANTHROPIC_API_KEY environment variable not found")
        self.client = anthropic.Anthropic(api_key=api_key)

    def predict(self, input: LLMInput) -> Optional[Message]:
        """Call Claude API with input to get a response.
        
        Args:
            input (LLMInput): Payload to send to Claude API,
                Consists of system prompt and a list of messages.
        
        Returns:
            Optional[Message]: Response from Claude as Message,
                or None, if Claude decided to not return a response
                based on the system prompt."""

        try:
            messages_dict = [message._asdict() for message in input.messages]

            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                system=input.system,
                messages=messages_dict
            )

            if not response:
                return None
            
            if response.role != "assistant":
                print(f"Warning: response role is not assistant: {response.role}")

            if not isinstance(response.content, list):
                return None

            if len(response.content) == 0:
                return None
      
            content = response.content[0].text
            if "empty string" in content:
                return None

            return Message(response.role, content)
        except Exception as err:
            print(f"Exception when calling Claude API: {err}")
        return None
