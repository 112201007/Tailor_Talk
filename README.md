How to run?
=============
uvicorn app:app --reload
streamlit run streamlit_app.py















curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
    "model": "gpt-4o-mini",
    "store": true,
    "messages": [
      {"role": "user", "content": "write a haiku about ai"}
    ]
  }'





=========
npm install openai

import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "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",
});

const completion = openai.chat.completions.create({
  model: "gpt-4o-mini",
  store: true,
  messages: [
    {"role": "user", "content": "write a haiku about ai"},
  ],
});

completion.then((result) => console.log(result.choices[0].message));

=========

pip install openai

from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
