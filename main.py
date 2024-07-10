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

from agent_types import Agent
from claude import Claude
from chatgpt import ChatGPT
from orchestration import agent_loop
import roles

claude = Claude()
chatgpt = ChatGPT()

shopkeeper = Agent(claude,
    "Shopkeeper",
    roles.shopkeeper_system_message,
    roles.shopkeeper_first_message)

customer = Agent(chatgpt,
    "Customer",
    roles.customer_system_message,
    roles.customer_first_message)
                         
agents = [shopkeeper, customer]

print("\nIt is a sunny day. A customer is approaching an ice cream truck.\n")
agent_loop(agents)
