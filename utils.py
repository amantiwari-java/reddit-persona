def build_prompt(posts, comments):
    content = "\n\n".join(posts + comments)

    prompt = f"""
You are an expert human behavior analyst.

Based on the following Reddit posts and comments, generate a complete **User Persona** that includes:

- Name (can be fictional)
- Age (estimated)
- Gender (if possible)
- Occupation (if inferred)
- Interests / Hobbies
- Personality Traits
- Political or Social Beliefs (if observable)
- Writing Style
- Any unique patterns or behavior

⚠️ For **each characteristic**, cite the post or comment that helped you conclude that information.  
Here is the user's activity:

\"\"\"{content}\"\"\"
    """
    return prompt
