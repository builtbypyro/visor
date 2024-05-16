from markdownify import markdownify as md
import tiktoken

def divide_chunks(l, n): 
    """
    Divides list into chunks of n length
    
    """
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
        
def prepare(content : str) -> list:
    """
    Converts provided html into markdown / LLM-Friendly content. In addition checks the token count, if the token count is too high it will split it into a list
    
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    content = md(content)
    tokens = encoding.encode(content)
    tokens_count = len(tokens)
    listcont = []
    cont = []
    if tokens_count > 3072:
        listcont = list(divide_chunks(tokens, 2048))
    
        for chunk in listcont:
            str(cont.append(encoding.decode(chunk)))
        
    if len(listcont) > 1:
        return cont
    
    listcont.append(content)
    return content
        
        
            
        
