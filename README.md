# Save-Heart

## Description

Is your heart healthy enough? Do you want to predict whether you risk a heat attack? Then this tool is for you!<br/>
Aim for this project is to use my ML skills to predict the chances of a person will suffer from a heart attack.<br/> 

## Project structure

```
  ├── Dataset/                Contains the dataset of save-heart.
  ├── media/                  Contains all media files for this project.
  ├── Notebooks/              Contains the jupyter notebook of save-heart.
      ├── save_heart.ipynb    The notebook.
      ├── dt_model.joblib     The saved model.
  ├── static/                 Contains the CSS files for web app.
      ├── index.css           Styling of the Homepage for the web app.
      ├── result.css          Styling of the Result page for the predictions.
  ├── templates/              Contains the HTML files for web app.
      ├── index.html          Homepage for the web app.
      ├── result.html         Result page for the predictions.
  ├── .gitignore              Ignored git files.
  ├── db.sqlite3              Database of Django project.
  ├── manage.py               Runner file of Django.
  ├── Procfile                Information for deployment.
  ├── README.md               Documentation of the project.
  ├── requirements.txt        The modules and their versions required to setup the project.
  ├── runtime.txt             Python runtime version.
```

## Datasets and Notebooks

- `save-heart.csv` is the dataset used for the notebook `save-heart.ipynb`
- `dt_model.joblib` is the dumped file made from `save-heart.ipynb`


## Prerequisites

### Software Needed

1. A web browser.
2. A standard code-editor (VS Code, Pycharm).
3. Python data science libraries / Anaconda

### Knowledge Needed

- Very basic understanding of git and github:

- For Visualisation and models implementation:

  1. Basic syntax and working of `python`.(This is a must)
  2. Basic knowledge of Data Science libraries like `numpy`, `pandas`, `matplotlib`, `seaborn`.
  3. Basic knowledge of `Scikit-learn`.
  4. Knowledge of various ML models. 
  5. Knowledge of Django.

- For the web app

  1. HTML
  2. CSS

## Attribute Information

1. age (in years)
2. sex (male=1, female=0)
3. cp: chest pain type
   -- Value 0: no pain
   -- Value 1: light pain
   -- Value 2: moderate pain
   -- Value 3: severe pain
4. resting blood pressure (in mm Hg on admission to the hospital)
5. serum cholestoral in mg/dl
6. fasting blood sugar in mg/dl (> 120  = 1, <= 120 = 0)
7. maximum heart rate achieved
8. exercise induced angina (yes = 1, no = 0)
9. thalassemia (normal = 0; fixed defect = 1 (no blood flow in some part of the heart), reversible defect = 2 (a blood flow is observed but it is not normal))
10. target (0 = less chance of heart attack, 1= more chance of heart attack)

## Home Page
<img width="1440" alt="Screenshot 2022-08-20 at 09 41 20" src="https://user-images.githubusercontent.com/76846542/185728502-eb780885-49ce-4b1c-9786-0f68671e33ba.png">

## Predictions

<img width="1440" alt="Screenshot 2022-08-20 at 09 41 34" src="https://user-images.githubusercontent.com/76846542/185728530-1d9b43dc-457f-4836-bc7a-beb0e5059f24.png">




