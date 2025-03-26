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

APP_PAGES = ["Upload CVs", "Evaluate Candidate", "Interview", "Overview"]

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
            "question": "PROGRAMMING - WARM UP\n\nHow do you rate your:\n\n- Python skills\n- SQL skills\n- Spark skills",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nWe have two approaches for programming in Python. A more Class-based approach or a more function-based approach. Which one do you prefer and why?\n\nAdvanced candidates are expected to mention that this depends on the situation and there is no **one single approach** to programming",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nBenefits of classes? What is the difference between an object and a class? What is the use of the `self` keyword in the class?\n\n**Advanced:** Can you change the word `self` and replace it for something else in Python? Why?",
            "answer": "",
            "score": 0,
            "feedback": "",
        },
        {
            "question": "PROGRAMMING - PYTHON\n\nHow do you integrate testing into you normal workflow? What libraries do you use in Python?\n\nWhat is a Mock and what is it's use?",
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
            "question": "DEEP DIVE - OPTION 1: Measurements\n\nWe have a sample of flights and their bookings over time for a certain time window. You have the number of passengers in the booking and the fare they paid, so you can construct the total income generated by the flight and the number of passengers you have at any moment in time. All flights have already departed. \n\nHalf of the flights have been assigned to a model, while the other half has been assigned to a different model.  \n\nHow do you determine which model is better?\n\n- How would you frame this problem? \n- Pay attention to clarifying questions asked by the candidate \n- How do you determine which model is better or worse? \n- What types of assumptions do you make in order to answer the question? \n- How do you quantify the uncertainty in the estimate? \n- How do you determine a good sample size for the experiment? \n- How would you report this to a technical audience? \n- How would you report this to a non-technical audience? ",
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
