# Methodology

## Research Question

How can agent-based AI tools help organize and summarize mental health research literature more efficiently?

## Project Design

This project is designed as an applied data science prototype. The goal is to evaluate whether AI-assisted workflows can support common literature review tasks in mental health research. The project begins with a simple baseline pipeline and will later compare that baseline to more advanced LLM-based or agent-based methods.

## Workflow

The current workflow includes the following stages:

1. **Data Collection**  
   An initial dataset of mental health literature records is used for prototype development. The dataset includes article titles, publication years, journals, topics, and abstracts.

2. **Preprocessing**  
   Article abstracts are cleaned using basic text preprocessing methods. This includes whitespace normalization and tokenization.

3. **Baseline Summarization**  
   A simple rule-based summarizer creates short summaries from article abstracts. This is not intended to be the final model. Instead, it provides a baseline for later comparison.

4. **Keyword Extraction**  
   The pipeline identifies keywords related to mental health and AI research, such as depression, anxiety, sleep, stress, literature review, and summarization.

5. **Evaluation Metrics**  
   The current evaluation includes basic quantitative metrics:
   - Abstract word count
   - Summary word count
   - Keyword count
   - Readability proxy

6. **Output Generation**  
   Results are saved as a structured CSV file so they can be reviewed, analyzed, and used in presentation materials.

## Mid-Semester Status

At the midpoint of the project, the baseline workflow has been created and tested on an initial dataset. This stage provides a working foundation for the second half of the capstone. The next phase will focus on expanding the dataset, testing LLM-generated summaries, and comparing the quality of different summarization approaches.

## Planned Evaluation Expansion

Future evaluation will include more qualitative criteria, such as:

- Accuracy of the summary
- Completeness of important findings
- Clarity and readability
- Usefulness for literature review organization
- Ability to preserve the meaning of the original article

These criteria will help determine whether AI-assisted workflows provide meaningful support for mental health literature review tasks.
