import openai

def generate_email_response(email_content, reply_content):
    openai.api_key = ''  # Replace with your OpenAI API key

    prompt = f"You received an email:\n\n{email_content}\n\nReply: {reply_content}\n\n"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
    )

    generated_text = response.choices[0].text.strip()
    
    # Check if response is incomplete and generate additional tokens if necessary
    while not (generated_text.endswith(".") or generated_text.endswith("?") or generated_text.endswith("\n")):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt + generated_text,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
        )
        generated_text += response.choices[0].text.strip()

    return generated_text

# Example usage
email_content = """
    Dear Utkarsh,

Good Morning!

We are thrilled to have you as a participant in the upcoming hackathon event, and we appreciate your enthusiasm for exploring innovative solutions. As part of the lab exercises and to ensure a seamless experience during the event, we kindly request your assistance in signing in to your AWS account using the provided CSV file.

In case you encounter any difficulties during the account sign-in process or have questions related to the AWS console, please don't hesitate to reach out to our organisers team. We are here to provide guidance and address any concerns you may have.

Thank you for your cooperation and active participation. Should you require any further information or assistance, please feel free to contact us. We wish you the best of luck in the hackathon and hope you have a rewarding and fulfilling experience.

Regards,
Anantha 
"""
reply_content = "Thank you for your help with aws access."
generated_response = generate_email_response(email_content, reply_content)
print(generated_response)
