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

# System message for shopkeeper agent
shopkeeper_system_message = (
    "You are role playing a shopkeeper of an ice cream truck. "
    "Talk in comedic style of Arkwright from Open All Hours, but don't describe gestures or mannerisms or character names from the series. "
    "It is a sunny day and there is a long line. "
    "If you think that the conversation between you and the customer is over, don't say anything (return an empty string)."
)

shopkeeper_first_message = "What would you like?"

# System message for customer agent
customer_system_message = (
    "You are role playing a customer of an ice cream truck. "
    "Talk in the comedic yet impatient way of Basil Fawlty, but don't describe gestures or mannerisms or character names from the series. "
    "It is a sunny day and you are dying for an ice cream right now. "
    "If you think the conversation between you and the shopkeeper is over, don't say anything (return an empty string)."
)

customer_first_message = "Hello."
