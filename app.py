import json
from fastapi import FastAPI

from domain.sentence.sentences import init_sentences
from domain.chatgpt.gpthandler import GPTHandler
from domain.correction.correction_payload import CorrectionPayload

app = FastAPI()
app.counter = 0
app.sentences = init_sentences()
app.gpt_handler = GPTHandler()


@app.get("/sentence")
async def generate_sentence():

    sentence = app.sentences[app.counter]

    print(f"sentence: {sentence}")

    app.counter = (app.counter + 1) % len(app.sentences)

    return {
        "sentence": sentence
    }


@app.post("/correction")
async def correct_sentence(correction_payload: CorrectionPayload):

    print(correction_payload)

    sentence = correction_payload.sentence_to_translate
    translation = correction_payload.translation_attempt

    correction = app.gpt_handler.correct_translation(sentence, translation)
    try:
        correction_dict = json.loads(correction.strip())
    except Exception as e:
        print("Invalid JSON first try. Trying to convert using ChatGPT")
        correction_processed = app.gpt_handler.convert_to_json(correction)
        try:
            correction_dict = json.loads(correction_processed.strip())
            print("Conversion successful")
        except:
            raise Exception("Wasn't able to convert")
        
    return correction_dict
