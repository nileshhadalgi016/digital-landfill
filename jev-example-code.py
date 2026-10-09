import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key or not api_key.strip():
    raise SystemExit(
        "Missing OPENROUTER_API_KEY. Set it in your environment or in a .env "
        "file beside this script, then run again."
    )

ticket_text = (
    "Hey support team, I bought your premium tier subscription an hour ago "
    "but my account is still showing the free trial. I am trying to export a "
    "client report for a presentation in 20 minutes! Please fix this or just "
    "cancel my payment."
)

response = requests.post(
    url="https://openrouter.ai/api/alpha/decisions",
    headers={
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json",
    },
    json={
        "model": "typesafe/jev-1.13",
        "state": ticket_text,
        "questions": {
            "category": {
                "type": "choice",
                "instructions": "Which department should handle this request?",
                "criteria": {
                    "billing": "Payment processing, billing errors, and refund requests.",
                    "technical_bug": "Application crashes, performance issues, or broken features.",
                    "feature_request": "Users suggesting improvements or additions to the app.",
                    "spam": "Unsolicited promotional content, ads, or junk messages.",
                },
            },
            "urgency": {
                "type": "score",
                "instructions": "How severe is the time-sensitivity or structural impact?",
                "criteria": [
                    "Low: Safe to handle during normal operating hours.",
                    "Medium: Important issue impacting workflow, but short-term workarounds exist.",
                    "High: Major failure blocking business operations or immediate tight deadline.",
                ],
            },
            "churn_risk": {
                "type": "noul",
                "instructions": "Is the customer explicitly threatening to cancel or demanding a refund?",
                "criteria": {
                    "true": "Explicit threat to cancel or demand for a refund.",
                    "false": "No explicit threat to cancel or demand for a refund.",
                },
            },
        },
    },
    timeout=60,
)
response.raise_for_status()
answers = response.json()["answers"]
category = answers["category"]

print("--- Jev Evaluation Results ---")
print(f"Assigned Category:  {category['choice']}")
print(f"Choice Confidence:  {category['probabilities'][category['choice']]:.2%}")
print(f"Urgency Index:      {answers['urgency']['score']:.2f} / 2.00")
print(f"Churn Probability:  {answers['churn_risk']['noul']:.2%}")
