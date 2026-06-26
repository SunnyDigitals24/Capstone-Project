# Literature Review Notes

## Project Context

This project focuses on the use of artificial intelligence tools to support literature review tasks in mental health research. The project is connected to several broader areas: mental health research, natural language processing, large language models, research automation, and agent-based AI workflows.

## Mental Health Literature Review Challenges

Mental health research is a broad and active area of study. Topics such as depression, anxiety, sleep, stress, and student well-being appear across psychology, public health, medicine, and education. Because the field is large, researchers often need to review many papers before they can identify common findings, compare methods, and understand where gaps exist. This process can be slow, especially when articles use different terminology or focus on overlapping but slightly different outcomes.

For this project, mental health literature is a strong use case because it connects to psychology and behavioral science while still allowing the use of data science methods. Literature review tasks can be treated as an information organization problem. Articles can be collected, cleaned, summarized, grouped by topic, and evaluated based on how well key details are extracted.

## AI-Assisted Literature Review

AI tools are increasingly being explored for research support tasks. In literature review settings, AI can help with article screening, keyword extraction, summarization, and topic organization. These tools may reduce the amount of time required for early-stage review work. However, they also introduce concerns related to accuracy, missing context, and overreliance on automated summaries.

Large Language Models are especially relevant because they can generate human-readable summaries and identify themes in complex text. At the same time, LLMs can produce incorrect or unsupported information, so any AI-generated output still needs to be reviewed by a human researcher. This project treats AI as an assistant rather than a replacement for human judgment.

## Agent-Based AI Workflows

Agent-based AI systems extend basic LLM use by organizing multiple steps into a workflow. Instead of only generating one summary, an agent-based system could retrieve articles, summarize abstracts, extract variables, organize findings, and prepare structured outputs. This makes agent-based systems a useful direction for literature review automation.

For the current stage of the capstone, the project begins with a baseline pipeline that performs simpler versions of these tasks locally. This creates a foundation that can later be compared with a more advanced LLM or agent-based workflow.

## Current Project Direction

The current project question is: How can agent-based AI tools help organize and summarize mental health research literature more efficiently? The early prototype focuses on building the basic workflow first: loading article data, generating summaries, extracting keywords, and saving structured results. The next stage will involve expanding the dataset and testing more advanced AI summarization methods.
