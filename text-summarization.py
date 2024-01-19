from transformers import pipeline

def summarize_text(text_needs_to_summarize):
    pipe = pipeline("summarization", model="facebook/bart-large-cnn")

    generated_text = pipe(text_needs_to_summarize)

    return generated_text



def main():
    print("Welcome to the summarization project you have 100 credits to begin and every summarization takes 25 credits")

    text_needs_to_summarize = input("Enter the text you would like to summarize: ")

    total_credit = 100

    while total_credit > 0:
        generated_text = summarize_text(text_needs_to_summarize)

        print(generated_text)

        retry = input("Do you want to try again? (yes/no)")

        if(retry == 'no'):
            print("Thank you!")
            break
        if(retry != 'yes'):
            print("Invalid input")
            break

        total_credit -= 25
        print(f"You have {total_credit} left")
    
    if(total_credit <= 0):
        print("You do not have enough credits")

if __name__ == '__main__':
    main()


