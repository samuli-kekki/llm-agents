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

from typing import List
from agent_types import Agent

def agent_loop(agents: List[Agent], max_iterations = 7):
    """Make agents communicate by passing
    output of one agent as the input to the next agent in the list."""

    if len(agents) < 2:
        print("we need at least two agents.")
        return
    
    # When calling Anthropic API
    # we need at least one user message.
    # Use first_message from second agent as the input
    # when calling the first agent for the first time.
    previous_agent_response_str = agents[1].first_message

    # This loop passes the output of an agent
    # as the input to the next agent.
    # It works well when there are two agents
    # having a dialogue.
    for _ in range(max_iterations):
        for agent in agents:
            response = agent.turn(previous_agent_response_str)
            previous_agent_response_str = response.content if response else None
            if not previous_agent_response_str:
                print(f"No response from {agent.name}, exiting the loop")
                break
            print(f"{agent.name}: {previous_agent_response_str}")
            print()
        if not previous_agent_response_str:
            break
