# Tunts.Rocks Internship Challenge 2024 (Dev Training Program)

## Summary

- [Quick start](#quick-start)
- [Useful links](#useful-links)
- [Challenge](#challenge)
- [Rules](#rules)
- [Preview](#preview)
- [Assessment criteria](#assessment-criteria)
- [Technologies](#technologies)
- [About the author](#about-the-author)



## Quick start

First of all, you need to have **Python** and **pip** installed in your machine.

Then clone the repository, using this command:

```bash
git clone https://github.com/gabrielsoarespebr/tunts-rocks.git
```

Open your Command Line Interface (CLI), and install the libraries:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread
```

*Note: If this command doesn't work, rewrite with **pip3** instead of **pip***

Now, run the main script:

```bash
python script.py
```

*Note: If you encounter the error below, it happens because the Google Sheets API has a limit on requests for free usage, as seen in the image.*

> [!CAUTION]
> gspread.exceptions.APIError: {'code': 429, 'message': "Quota exceeded for quota metric 'Read requests' and limit 'Read requests per minute per user' of service 'sheets.googleapis.com' for consumer 'project_number:704566982728'.", 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'RATE_LIMIT_EXCEEDED', 'domain': 'googleapis.com', 'metadata': {'quota_location': 'global', 'quota_limit_value': '60', 'service': 'sheets.googleapis.com', 'consumer': 'projects/704566982728', 'quota_metric': 'sheets.googleapis.com/read_requests', 'quota_limit': 'ReadRequestsPerMinutePerUser'}}, {'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Request a higher quota limit.', 'url': 'https://cloud.google.com/docs/quota#requesting_higher_quota'}]}]}

![Google Sheets API limit requests](https://i.ibb.co/ZN3LQrG/google-Sheets-Limit.png)

[Back to summary](#summary)



## Useful links

- [Google Sheets](https://docs.google.com/spreadsheets/d/1jA9bxN9YNrEqZA_WQMBolywSyjpU4HPxVN1TAxPkdtg/edit#gid=0)
- [GitHub repository](https://github.com/gabrielsoarespebr/tunts-rocks)

[Back to summary](#summary)



## Challenge

Create an application in a programming language of your choice. The application should be able to read a Google Sheets spreadsheet, fetch the necessary information, calculate, and write the result back to the spreadsheet.

[Back to summary](#summary)



## Rules

Calculate the situation of each student based on the average of the 3 exams (P1, P2, and P3), according to the table:

| Arithmetic mean (m)  | Situation            |
| -------------------- | -------------------- |
| m < 50               | "Reprovado por Nota" |
| 50 <= m < 70         | "Exame Final"        |
| m >= 70              | "Aprovado"           |

*Note: The problem statement refers to grades from 0 to 10, but the Google Sheets table refers to grades from 0 to 100. Considering this difference, I followed the 0-100 model.*

- If the number of absences exceeds 25% of the total number of classes, the student will be marked as "Reprovado por Falta", regardless of the arithmetic mean.

- If the status is "Exame Final" it is necessary to calculate the "Nota para Aprovação Final"(naf) for each student according to the following formula:

`5 <= (m + naf)/2`

- If the student's status is different from "Exame Final", fill the "Nota para Aprovação Final" field with 0.

- Round the result to the next integer (round up) if necessary.

- Use log lines to track the application's activities.

The texts in the source code (attributes, classes, functions, comments, etc.) should be written in English, except for the identifiers and predefined texts in this challenge.

[Back to summary](#summary)



## Preview

![Google Sheets automation with Python](https://i.ibb.co/yqLrpYG/Design-sem-nome.gif)

[Back to summary](#summary)



## Assessment criteria

- [x] Good understanding of the problem to be solved;
- [x] Success in implementing the functionality;
- [x] Source code structure;
- [x] Documentation and use of best practices;
- [x] Utilization of basic development tools.

[Back to summary](#summary)



## Technologies

- Programming language: **Python**
- Libraries:
  - **oauth2**: Google OAuth 2.0 Library for Python
  - **gspread**: Google Spreadsheets Python API
  - **math**: This module provides access to the mathematical functions defined by the C standard
- Version control: **Git**

[Back to summary](#summary)



## About the author

- [LinkedIn](https://www.linkedin.com/in/gabrielsoarespebr/)
- [GitHub](https://github.com/gabrielsoarespebr)
- [Portfolio](https://gabrielsoares.vercel.app)

[Back to summary](#summary)