# 25 AI Concepts in 60 Seconds

## 1. Tokens & Embeddings
Text doesn't go into a model as words. It gets chopped into sub-word chunks called tokens, and each token becomes a list of numbers, a vector. Words with similar meaning end up as vectors that sit close together in that space. That's why a model "knows" king and queen are related without ever being told the definition. It just sees the coordinates.

![Tokens & Embeddings](1_tokens_embeddings.png)

## 2. Attention Mechanism
This is how a model figures out which words matter to which other words. For every token, it calculates a weight against every other token in the sentence, deciding how much focus to give each one. In "the trophy didn't fit in the suitcase because it was too big," attention is what lets the model figure out "it" means the trophy, not the suitcase.

![Attention Mechanism](2_attention.png)

## 3. Transformers
Before transformers, models read text one word at a time, left to right, like a slow scanner. Transformers throw that out. They read the entire sequence in parallel using attention, so every word can look at every other word at once. That's the single architectural shift that made GPT, Claude, and basically every modern LLM possible.

![Transformers](3_transformers.png)

## 4. Pre-training vs Fine-tuning
Pre-training is the expensive part: feed the model a massive chunk of the internet so it learns grammar, facts, and reasoning patterns in general. Fine-tuning comes after. It's a smaller, targeted training pass that shapes that general model into something specific, like a coding assistant or a medical Q&A bot.

![Pre-training vs Fine-tuning](4_pretrain_finetune.png)

## 5. RLHF & DPO
A raw pre-trained model just predicts the next word. It doesn't know how to be helpful or polite or stay on topic. RLHF (Reinforcement Learning from Human Feedback) and DPO (Direct Preference Optimization) are the training steps that fix that. Humans rank model outputs, and the model gets optimized to produce answers people actually prefer. This is the layer that turns a text predictor into an assistant.

![RLHF & DPO](5_rlhf_dpo.png)

## 6. Quantization
Model weights are normally stored as 16-bit floating point numbers, which takes a lot of memory. Quantization compresses those weights down to 8-bit or even 4-bit integers. You lose a small amount of precision, but you cut VRAM usage massively, which is why you can run a 7B or even 70B parameter model on a regular laptop or a single GPU instead of a data center rack.

![Quantization](6_quantization.png)

## Outro & CTA
Follow for Part 2. Comment AI and I'll send you the full list.
