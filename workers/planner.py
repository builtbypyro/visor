from util.gpt import generate

def initialPlan(task, model = "gpt-4-32k"):
    query = [{
        "role": "user",
        "content": r"For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps. The format should be: Step: *stephere*, stephere representing the step you believe you should do. Return a valid json list or else bad things will happen. Only return the json list and nothing else. please take note that the step keyword shouldn't have a number and these steps will be used by another AI to accomplish the task. Therefore do not include things like 'of your choice' etc. You have common shortcuts at your disposal. If you want to open an internet browser, say chrome. To navigate to a certain website, just say the domain of the website excluding https:// and nothing else in that step Do not say 'go to youtube.com' or 'navigate to google.com' just say youtube.com or google.com respectively. do not say 'open chrome', just say chrome. If you do not do this then bad things will happen. Do not use any quotes in your step instructions."

    },
    {
        "role": "user",
        "content": f"The objective given by the user is: {task}"
    }]
    
    
    
    return generate(messages=query, model=model)
    
    
def planAgain(task, plan, completed, model = "gpt-4-32k"):
    query = {
        "role": "user",
        "content": 
            
        f"""
        For the given objective, come up with a simple step by step plan. \
        This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
        The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

        Your objective was this:
        {task}

        Your original plan was this:
        {plan}

        You have currently done the follow steps:
        {completed}

        Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.
        
        """
    }
    
    
