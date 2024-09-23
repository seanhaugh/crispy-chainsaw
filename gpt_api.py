# gpt_api.py

import openai

# Replace with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_meta_title(keyword):
    prompt = f"Create an engaging meta title for the keyword: '{keyword}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def generate_headings(all_headings, keyword):
    prompt = (
        f"Using the following headings from competitors:\n{all_headings}\n"
        f"Consolidate and create the best set of headings for a page about '{keyword}', "
        "favoring user experience."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].text.strip().split('\n')

def generate_faq_questions(keyword, existing_headings):
    prompt = (
        f"Generate FAQ questions related to '{keyword}' that are not covered in these headings:\n"
        f"{existing_headings}"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip().split('\n')
