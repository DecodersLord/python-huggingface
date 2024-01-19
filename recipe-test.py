from transformers import pipeline
import re

def answer_question(question):
    # Load the pre-trained question-answering pipeline
    pipe = pipeline("text2text-generation", model="flax-community/t5-recipe-generation")

    # Get the answer
    result = pipe(question)
    
    return result

def get_user_input():
    
    print("Enter the ingredients that you have handy:")
    question = input()
    
    return question

def main():

    question = get_user_input()
    
    # Get the answer using the QA function
    answer = answer_question(question)
    
    generated_recipe = answer[0].get('generated_text','')
    # Split the generated text into lines
    lines = generated_recipe.split('\n')

    lines = lines[0]
    
    print(lines)

    pattern = re.compile(r"title:\s*(?P<title>.*?)\s*ingredients:\s*(?P<ingredients>.*?)\s*directions:\s*(?P<directions>.*)\s*", re.DOTALL)

    # Match the pattern in the text
    match = pattern.match(lines)

    # Extract the groups
    title = match.group('title').strip()
    ingredients = match.group('ingredients').strip()
    directions = match.group('directions').strip()

    # Print the results
    print(f"Title: {title}")
    print(f"Ingredients:\n{ingredients}")
    print(f"Directions:\n{directions}")


if __name__ == "__main__":
    main()
