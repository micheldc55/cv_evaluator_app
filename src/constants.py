BASE_DIR = "candidates"

# used to keep our status names consistent
APPROVED = "approved"
REJECTED = "rejected"
PENDING = "pending"
SKIPPED = "skipped"

STATUS_COLOR_MAPPING = {
    "APPROVED": "#2E8B57",
    "REJECTED": "#D32F2F",
    "PENDING": "#FBC02D",
    "SKIPPED": "#757575",
}

PDF_WIDTH = 1500
PDF_HEIGHT = 1500

PAGE_UPLOAD_CV = "Upload CVs"
PAGE_EVALUATE_CANDIDATE = "Evaluate Candidate"
PAGE_INTERVIEW_1 = "Interview 1"
PAGE_INTERVIEW_2 = "Interview 2"
PAGE_OVERVIEW = "Overview"
PAGE_EXPORT_BASE_QUESTIONS = "Export Questions"

APP_PAGES = [
    PAGE_UPLOAD_CV, 
    PAGE_EVALUATE_CANDIDATE, 
    PAGE_INTERVIEW_1, 
    PAGE_INTERVIEW_2, 
    PAGE_OVERVIEW,
    PAGE_EXPORT_BASE_QUESTIONS
]

#### DOCUMENT CONFIGS
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

STRICTNESS_LEVELS = ["Very Strict", "Moderately Strict", "Moderately Lenient", "Very Lenient"]

#### INTERVIEW PRE-LOADED QUESTIONS:
BASE_QUESTIONS = {
    "questions": [
        {
            "question": "ABOUT THE TEAM: \n\nWe have a Data & BI team with over 110 people, distributed across different roles such as Data Scientists (DS), Data Analysts (DA), Optimization Experts (OE), Data Engineers (DE), Database Administrators (DB Admins), and BI Developers. \n\nIn our Madrid office, we have around 40 team members, including six Data Scientists. We also have teams in Dublin and Wroclaw. \n\nRegarding our company structure, we organize our work by projects. Data Scientists often take on the role of Project Leads, meaning they report directly to the Head of DS and have responsibilities beyond just technical work. \n\nOur main internal customers are from the Commercial department (focus on pricing, demand estimation, experiment design) but also there are other projects for Operations (scheduling, OTAs identification...) or Engineering (maintenance...) ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "Describe the process:\n- Looking for a DS with 2-3 years of experience\n- Experience in demand estimation / dynamic pricing is values\n- Experience in Experiment design is valued\n- Experience in ML project is valued",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STEPS OF THE PROCESS\n\n- First technical round\n- Second consists of a take-home exercise (1-2 days of work)\n- Second technical interview focused on the excercise\n- Third and final interview with the Head of DS and possibly DS Team Lead",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "CANDIDATE PRESENTS ITSELF:\n\n- Previous related projects\n- Tech Stack\n- Cloud Stack\n- Experience presenting to Stakeholders\n- What will you contribute to the team? Why should we choose you?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "ROUND OF TECHNICAL QUESTIONS: Now, we will move on to the technical part of the interview. We will split them into different blocks (Stats&ML, CS diving more into python, SQL, and coding in general)  and finally a business / practical case to think about.  \n- For each question, please try to keep your responses quick and concise—ideally around 2 to 3 minutes per question. The goal is not just to check technical knowledge but also to evaluate your problem-solving approach and communication skills. Probably for the business / practical cases at the end you can extend a bit more, \n- Let’s get started! ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STATS: Mean vs Median. Pros and Cons of each.",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STATS: Imagine you have a single feature that is current_price and you want to explore it. How would you do an EDA on it? Which things would you look at? Which plots would you use?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STATS: Now imagine you have two distribution of current_price and you want to compare them. How would you do it? Which things would you look at? Which plots would you use?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STATS: Talking about statistical distributions, can you name a few? Which ones are the most common? \n\n- Which would you use in case you want to model number of reservations in a time interval? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "STATS: What is a normal distribution? Which are the most important properties?  How do you identify if data follows a normal distribution?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "Now let's move to ML topic: Let's start with the basics (Linear Regression). Can you explain how it works? What are the assumptions behind it? Which are the things you look in the output? \n\n- How do you interpret the coefficients? \n- Is there something i can look to see if a feature has effect in the response variable? \n- How do you interpret the p-value?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "ML: let's move to tree-based models and boosting? Can you explain how they work? Which algorithms are you familiar? \n- How do you handle categorical features (e.g PostalCode or Province) that have many values? \n- How do you handle missing values? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "ML: Overfitting vs Underfitting. Can you explain the difference? How do you identify it? How do you solve it? \n- Do you know any parameter that can help you to avoid overfitting in a boosting model?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "ML: Model evaluation and interpretability. Can you name some metrics you use to evaluate a model? \n- What is the difference between precision and recall? \n- In case you need to explain how the model works to a non-technical audience, how would you do it? \n- In case you need to explain how the model works to a technical audience, how would you do it? \n- Do you know any library that can help you with this?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - WARM UP\n\nHow do you rate your:\n\n- Python skills\n- SQL skills\n- Spark skills",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nIn Python, you can approach problem solving using class-based (object-oriented) designs or functional programming paradigms. Describe a scenario in a data science project (for example, in experiment design or pricing algorithms) where you would favor one approach over the other. What trade-offs did you consider regarding maintainability, performance, and testability",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nExplain the benefits and potential pitfalls of using classes in Python. What is the role of the self parameter in class methods, and can you change its name without breaking functionality? Discuss any implications of doing so in a large-scale, collaborative codebase.\n\nWhen would you use abstract classes?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nHow do you integrate testing into your regular Python development workflow, particularly when building data pipelines or experimental frameworks? Describe your experience with libraries such as unittest, pytest, or mocking frameworks. How do you design tests that validate both the logic and the data integrity in your pipelines?\n\nIn your testing workflow, how do you use mocking to isolate dependencies? Briefly explain what a mock is and provide an example of when you'd use it to simulate behavior in your code.",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nYou need to write a Python script that:\n\n1.  Fetches data from an API\n2.  Transforms the data\n3.  Saves the result to a CSV file.\n\nHow would you structure this code to make it testable and maintainable?\n\nDescribe the key functions or modules you’d create and how you’d organize the code.",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": 'PROGRAMMING - PYTHON\n\nClean Coding Practices:\n\n1) Can you name a few? e.g: Functions do one thing, clean names, avoid duplication, etc.\n2) Can you provide an example of how you integrate them into your workflow?\n3) Imagine you are reviewing a PR and you see this function:\n\n```python\ndef get_flight_output_plus_tax(flight_key):\n    data = get_flight_from_dynamo_db(flight_key)\n    return data["price"] * 1.22\n```',
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\n**Advanced Only:** What is the difference between doing a = b when b is mutable versus when b is immutable?\n\nHow does this affect your day-to-day work as a DS?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {"question": "PROGRAMMING - SQL\n\nWhat is a primary key?", "answer": "", "score": 0, "feedback": ""},
        {
            "question": "PROGRAMMING - SQL\n\nWhat is the difference between a Table and a View in SQL? \n\n**Next level:** What about a materialized view?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - SQL\n\nWhat is a **HAVING** clause and how do you use it?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - SQL\n\nThere is a table called bookings with these columns:\n\t•\tflight_id\n\t•\tbooking_id\n\t•\tfare\n\t•\tbooking_date\n\t•\tpassenger_name\n\nEach row represents one passenger's booking on a particular flight.\n\n**The Task**\n\nFor each flight, retrieve the top 3 bookings by fare (i.e., the 3 most expensive tickets). Each output row should still show the detailed booking information (like booking_id, fare, and passenger_name), not just an aggregate.",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - SPARK\n\nWhat is the difference between an action and a transformation? What is lazy evaluation in Spark? \n\n- Examples of transformations (lazy): select(), groupBy().\n\n- Examples of actions (executed): show(), collect(), count(), take(), first(), etc.",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - SPARK\n\nYou have a Dataset with 30M rows that you need to explore.\n\n- How do you tackle it?\n- You have to visualize some plots. How do you tackle that?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - SPARK\n\n**Advanced:** How does sampling work in Spark? What is the difference between sampling in Pandas vs Spark? Why is it non deterministic?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - DOCKER\n\nExperience with Docker?  \n\n**Beginner:** Name some docker commands \n\n**Interm:**  Difference between an image and a container \n\n**Advanced:** How do the Docker build layers work? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - GIT\n\n- You are working with a colleague, how do you integrate his changes to your branch? \n- What is a conflict? How do you handle it? \n- What is the difference between a commit and a push? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "DEEP DIVE - OPTION 1: Measurements\n\nImagine we have two models producing prices for our flights and we need to evaluate which one is the best for our company. \n\nFor simplicity, imagine the models are very similar in terms of training set and algorithm perspective and we just need to compare the results. So, e.g we could have 10000 flights priced by model A and 10000 flights priced by model B and imagine these flights have already departed so we can now all the information about bookings. \n\nHow do you determine which model is better?\n\n- Which would be the KPI that you would use for that? \n- How do you determine which model is better or worse and which one should be promoted? \n- What types of assumptions do you make in order to answer the question? \n- Imagine the results are very similar, how do you decide then? If model A has 1000€ in rev per flt and model B has 1005€, do you think is enough? If we rerun the experiment again the result would be the same? How do you quantify the noise or uncertainty in the estimation? \n- How do you determine a good sample size for the experiment? \n- How would you report this to a technical audience? \n- How would you report this to a non-technical audience? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "DEEP DIVE - OPTION 2: Predictin Cancelled flights\n\nWe are interested in determining if a flight will be cancelled ahead of time. Assume we have a label for flights (cancelled/not cancelled) and we want to predict whether a flight will be cancelled or not. Cancellations are defined as a flight that will not depart and will not be rescheduled. \n\nWe want to make an “early” estimation of potential cancellations 60 days before departure, and a “close” estimation of cancellations 3 days before departure. \n\nWhat are some relevant features you think might be helpful in determining if a flight will be cancelled or not? E.g: \n\n- Numpax \n- Cancellations in flights departing from or to the same airport \n- Natural phenomena / climatic conditions \n- Cancellations in previous similar historic flights \n- Contracts with airports \n- Crew availability / Delays / Strikes \n\n**Interesting questions:**\n\n- Do you expect the two scenarios to behave similarly? \n- Do you think this model would need to be explainable? Why? \n- What metrics would you use to evaluate this model? ",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
    ],
    "global_feedback": "",
}

### SECOND INTERVIEW QUESTIONS:
BASE_SECOND_INTERVIEW_QUESTIONS = {
    "questions": [],
    "global_feedback": "",
}
