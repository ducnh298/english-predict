# Auto Completion using N-Gram Models

💬An Auto-Complete program using N-Gram Models. You can view the deployed website [here](https://autocomplete-ngram.herokuapp.com/).

![](https://github.com/SauravMaheshkar/Auto-Completion-using-N-Gram-Models/blob/master/assets/app.png)

The dataset used for obtaining the n-grams and the vocabulary can be found [here](https://www.kaggle.com/crmercado/tweets-blogs-news-swiftkey-dataset-4million) and was uploaded by [Carlos Mercado](https://www.linkedin.com/in/crmercado/).

# How to Reproduce

## Docker Approach

```
docker pull docker.pkg.github.com/sauravmaheshkar/auto-completion-using-n-gram-models/autocomplete:v0.1
```

## Conda Approach

```
mkdir <project_name>
cd <project_name>
git init
git clone https://github.com/SauravMaheshkar/Auto-Completion-using-N-Gram-Models.git
conda env create -f environment.yml
conda activate ac
```
