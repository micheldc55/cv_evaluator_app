# CV evaluator app

The purpose of this small repo is to have a place where we can quickly and effectively review CVs and add/track comments for each candidate


## Set up with `uv`

Apologies for any confusion in my previous instructions. Given the new information that your uv.lock file is present in version control and you’ve made changes to your pyproject.toml, here’s the updated process to set up your environment and run your Streamlit app using uv:

Setting Up and Running the CV Evaluator App with uv

### Clone the Repository

If you haven’t already cloned your repository, execute:

```bash
git clone https://github.com/micheldc55/cv_evaluator_app.git
cd CV_EVALUATOR_APP
```

You can also do this directly from your IDE of choice by cloning the repository using the url above in the GUI.

### Install uv

If uv isn’t installed on your system, install it using:

```bash
pip install uv
```

### Set Up the Virtual Environment and Install Dependencies

Since the uv.lock file is present, synchronize your environment to match the locked dependencies:

```bash
uv sync
```

This command will:
	•	Create a virtual environment (.venv/).
	•	Install all dependencies as specified in the uv.lock file.

Note: If you’ve made changes to the pyproject.toml and need to update the lockfile accordingly, run:

```bash
uv lock
```

Then, synchronize the environment again:

```bash
uv sync
```

4. Activate the Virtual Environment

To activate the virtual environment, use:

- macOS/Linux:

```bash
source .venv/bin/activate
```

- Windows (PowerShell) 🤮:

```bash
.venv\Scripts\Activate
```



5. Run the Streamlit App

With the virtual environment activated, start the app:

```bash
streamlit run app.py
```

Alternative: Run Without Activating the Virtual Environment

If you prefer to run the app without explicitly activating the virtual environment, use:

```bash
uv run streamlit run app.py
```

This command ensures that streamlit runs within the context of the uv-managed environment.

### Quick reference

For quick reference, execute the following commands in order:

```bash
git clone https://github.com/micheldc55/cv_evaluator_app.git
cd CV_EVALUATOR_APP
pip install uv
uv sync
uv run streamlit run app.py
```

Important: Ensure that your pyproject.toml and uv.lock files are up-to-date and consistent. If you’ve added or removed dependencies, always run uv lock followed by uv sync to update the lockfile and synchronize your environment.
