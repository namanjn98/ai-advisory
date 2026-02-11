from typing import List, Dict, Any


def build_meta_prompt(original_query: str, responses: List[Dict[str, Any]]) -> str:
    """Build Level 2 meta-prompt for consensus evaluation."""

    # Build responses section
    responses_text = ""
    for i, resp in enumerate(responses, 1):
        responses_text += f"\n### Response {i} (from {resp['name']})\n"
        responses_text += f"{resp['content']}\n"

    prompt = f"""You are participating in a consensus evaluation round. Multiple AI models were asked the following question:

**Original Query:** {original_query}

Below are the responses that were selected for evaluation:
{responses_text}

Please perform a comprehensive evaluation:

1. **Rating**: Rate each response on a scale of 1-10 with justification
2. **Agreement Analysis**: Identify key points where responses agree
3. **Disagreement Analysis**: Identify key points where responses disagree
4. **Pros & Cons**: List pros and cons of each response
5. **Consensus Answer**: Synthesize the best elements from all responses into a final, comprehensive answer

Be thorough, analytical, and provide a clear consensus answer at the end."""

    return prompt
