from pydantic import BaseModel

class CorrectionPayload(BaseModel):
    sentence_to_translate: str
    translation_attempt: str