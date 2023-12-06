from domain.chatgpt.constants import Roles

def generate_correction_prompt(sentence_to_translate: str, translation_attempt: str):

  return [
      {
          "role": Roles.USER.value,
          "content": f"""
  Correct my translation from portuguese to english. 
  List out each and every one of the grammatical errors I did and comment on those errors. 
  If there aren't any errors, do not list anything.

  Portuguese sentence to translate: ```{sentence_to_translate}```
  My English translation attempt: ```{translation_attempt}```

  """
      }
  ]

def generate_formatting_prompt(correction_prompt: list, correction: str):
   
  return correction_prompt + [
     {
        "role": Roles.ASSISTANT.value,
        "content": correction
     },
     {
        "role": Roles.USER.value,
        "content": """
Format the previous response in a JSON with the keys:

- original_sentence: the original portuguese sentence
- translation_attempt: my user translation attempt
- is_correct: a boolean that is true if the translation_attempt is correct
- corrected_translation: the corrected version of the user translation. if is_correct is true, it's the same as the translation_attempt.
- errors: an array of objects with keys "sentence_with_correction", "type" and "comment". "sentence_with_correction" is the full sentence with this correction and every other correction made before this. "comment" is the comments you made before regarding the error. "type" is the generic grammatical subject this specific errors falls into.
- general_comments: an array of strings with each paragraph not in the errors array.

if there aren't any errors, output errors as an empty array.
Do not output anything other than the JSON object I asked.
"""
     }
    
  ]