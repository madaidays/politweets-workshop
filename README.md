# politweets

Politweets is an AI project to get the closer tweet from Spanish politician to a given query

## Usage

### Download Pretrained Model

https://storepolitweets.blob.core.windows.net/models/pretrained/wiki.es.vec

### Conda setup

#### Create conda environment

```bash
conda env create -f environment.yml
```

#### Activate conda environment

```bash
source activate politweets
```

#### Add conda environment to jupyter notebook

```bash
python -m ipykernel install --user --name politweets --display-name "Python (politweets)"
```

## Links

Some of you asked in the meetup about the deploy steps. Here there is the tutorial you can follow to deploy models using Azure ML Services :)

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where
