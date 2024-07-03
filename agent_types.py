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

import anthropic
from abc import ABC, abstractmethod
from typing import NamedTuple, List, Optional
import os

class Message(NamedTuple):
    """Encapsulates the messages to send to the LLM.

    Attributes:
        role (str): Role of the message
        content (str): Content of the message
    """

    role: str
    content: str

class LLMInput(NamedTuple):
    """Input when calling LLM API.

    Attributes:
        system (str): System role to send to the LLM API
        messages (List[Message]): List of messages to send to the LLM API
    """

    system: str
    messages: List[Message]

class LLM(ABC):
    """Abstract base class for an LLM.
    It contains one method, predict."""

    @abstractmethod
    def predict(self, input: LLMInput) -> Optional[Message]:
        """Calls LLM API with input to get a response.
        
        Args:
            input (LLMInput): Payload to send to the LLM API,
                Consists of system role and a list of messages.
        
        Returns:
            Optional[Message]: Response from the LLM as Message,
                or None, if the LLM decided to not return a response
                based on the system role.
        """

        pass

class Claude(LLM):
    """A wrapper for Claude SDK.
    Helps with sending a list of messages to Claude
    and handling the response."""

    def __init__(self):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise KeyError("ANTHROPIC_API_KEY environment variable not found")
        # Anthropic client attempts to reads ANTHROPIC_API_KEY too
        # but I added a check to make it clear for the reader that it is needed.
        self.client = anthropic.Anthropic(api_key=api_key)

    def predict(self, input: LLMInput) -> Optional[Message]:
        """Calls Claude API with input to get a response.
        
        Args:
            input (LLMInput): Payload to send to Claude API,
                Consists of system role and a list of messages.
        
        Returns:
            Optional[Message]: Response from Claude as Message,
                or None, if Claude decided to not return a response
                based on the system role."""

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

class Agent:
    """A simple 'agent' that uses previous agent's
    response as the input for itself.
    
    Attributes:
        llm (LLM): object that implements the LLM interface
        name (str): Name of the agent
        system (str): System role of the agent
        first_message (str): If needed, agent can use this string to initiate a dialog
        messages (List[Message]): Current state of the agent, and is sent to LLM"""

    def __init__(self, llm: LLM, name: str, system: str, first_message: str):
        self.llm = llm
        self.name = name
        self.system = system
        self.first_message = first_message
        self.messages: List[Message] = []

    def turn(self, previous_agent_response: str) -> Optional[Message]:
        """Take turn by first adding the previous agent's response
        to the state and then calling the LLM to get response for this agent.
        
        Args:
            previous_agent_response (str): Response from the previous agent in the list
                as a string
                
        Returns:
            Optional[Message]: Response from this agent's LLM"""

        message = Message("user", previous_agent_response)
        self.messages.append(message)
        response = self.llm.predict(LLMInput(self.system, self.messages))
        if response:
            self.messages.append(response)
        return response
