import requests
from util.format import prepare
from util.gpt import generate

DEFAULT_PROMPT  = """

As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:

1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.

2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

3. Rely strictly on the provided text, without including external information.

4. Format the summary in paragraph form for easy understanding.

5. Do not speak to the user, you exist solely to output summaries.

6. Make it relatively long and filled with detailed, but no superfluous text. Include details about every point such as specifics of what, why, when, how, etc.


By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.


The text you will summarize is as follows, it is from a webpage and in Markdown format.
"""

def summarize(content, prompt = DEFAULT_PROMPT):
    """
    Returns a summary of the content provided with the prompt provided, if not provided, default prompt will be used
    """
    
    query = [
        {
        
            "role": "user",
            "content": prompt
        }
        ]
    
    if len(content) > 1:
        for chunk in content:
            query.append(
                {
                    "role": "user",
                    "content": r"" + chunk
                }
            )
    return generate(query)