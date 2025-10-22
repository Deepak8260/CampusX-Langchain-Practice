from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

class Review(BaseModel):
    key_themes:list[str] = Field(description="A list of key themes discussed in the review")
    summary:str = Field(description="A brief summary of the review")
    sentiment: Literal['positive' , 'negative' , 'neutral'] = Field(description="The sentiment of the review")
    rating:Optional[int] = Field(description="An optional rating from 1 to 5")
    pros:Optional[list[str]] = Field(description="A list of pros mentioned in the review")
    cons:Optional[list[str]] = Field(description="A list of cons mentioned in the review")
    author:Optional[str] = Field(description="The name of the review author")

strctured_model = model.with_structured_output(Review)

result = strctured_model.invoke("""After using the 'AuraFit Pro' Smartwatch for over a month, I'm mostly satisfied, earning it a solid 4/5 stars. The battery life is truly a game-changer; it easily lasts 10 days, which is much better than the competition. The health tracking is also incredibly accurate, especially the sleep monitoring. However, I have two minor gripes. Firstly, the companion mobile app is buggy and frequently crashes when syncing data. Secondly, the design, while durable, is a bit too bulky for smaller wrists. I'd definitely recommend it for its core functionality and longevity. - Review by Sarah M""")
print(result)