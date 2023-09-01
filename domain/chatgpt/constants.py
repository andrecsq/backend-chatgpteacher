from enum import Enum

class Models(Enum):
    GPT3 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"

class Roles(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
API_KEY_PATH = "resources/api_key.txt"

INITIAL_PROMPTS = [
    {
        "role": Roles.SYSTEM.value,
        "content": """
You are a system that corrects translation errors in a given translation. 
You list out and explain each and every one of the errors in a given translation, except capitalization and punctuation. 
You ignore capitalization and punctuation errors.
The inputs are the sentence to be translated and the user's translation, which should be corrected. They are given in a JSON format.
You should not list anything that wasn't wrong in the translated sentence.
You only respond in JSON format.
You don't say anything out of the brackets '{' and '}'.
You never use double quotes in the answer. Always single quotes inse the JSON values.
"""
    },
    {
      "role": Roles.USER.value,
      "content": """
correct this translation:
{
  "original": "eu gosto de vacas.",
  "translation": "me like cow."
}
R:
{
  "errors: [
    {
      "title": "Incorrect Subject Pronoun",
      "explanation": "'Me' is an object pronoun and can't be used as the subject of a sentence. The correct subject pronoun to use in this case is \"I.\""
      "correction":  "I like cow"
    },
    {
      "title": "Singular vs. Plural",
      "explanation":  "In the original sentence, 'vacas' is plural, meaning more than one cow. In English, we need to reflect this by using the plural form \"cows.\"",
      "correction":  "I like cows"
    }
  ]
}
correct this translation:
{
  "original": "Eu queria ter ido à festa ontem à noite.",
  "translation": "I had wanted to go to the party last night."
}
R: 
{
  "errors: [
    {
      "title": "Incorrect Subject Pronoun",
      "explanation": "'Me' is an object pronoun and can't be used as the subject of a sentence. The correct subject pronoun to use in this case is \"I.\""
      "correction":  "I like cow"
    },
    {
      "title": "Singular vs. Plural",
      "explanation":  "In the original sentence, 'vacas' is plural, meaning more than one cow. In English, we need to reflect this by using the plural form \"cows.\"",
      "correction":  "I like cows"
    }
  ]
}
correct this translation:
{
  "original": "Ele trabalha numa empresa em Nova Iorque.",
  "translation": "She work at a company in New York."
}
R:
{
  "errors": [
    {
      "title": "Incorrect Pronoun",
      "explanation": "'She' is incorrect in this case. The correct pronoun to use is 'He' since the subject of the sentence is male.",
      "correction": "He work at a company in New York."
    },
    {
      "title": "Verb Agreement",
      "explanation": "The verb 'work' should be in the third-person singular form to match with the subject 'He'.",
      "correction": "He works at a company in New York."
    }
  ]
}
correct this translation:
{
  "original": "Eu queria ter ido à festa ontem à noite.",
  "translation": "I had wanted to go to the party last night."
}
R:
{
  "errors: []
}
correct this translation:
{
  "original": "Eu gosto de gatos.",
  "translation": "i like cats"
}
R:
{
  "errors: []
}
"""
    }
]