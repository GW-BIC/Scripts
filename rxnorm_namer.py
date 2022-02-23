import requests
import json
import pandas as pd
import time
import tqdm


def main():

    """
    Accepts csv file containing names of drugs, returns ingredients (generic names, combinations etc) in output.csv
    Uses RxNav REST API to retrieve ingredients
    """

    counter = 0
    filename = 'drugs.csv'
    df = pd.read_csv(filename)
    headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                            'AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/45.0.2454.101 Safari/537.36')
            }
    for index, row in tqdm.tqdm(df.iterrows(), total=df.shape[0]):
        if counter < 15:
            drug = row['drugname']
            response = requests.get('https://rxnav.nlm.nih.gov/REST/drugs.json?name={}'.format(drug), headers=headers)
            readme = json.loads(response.text)
            counter += 1
            try:
                ingredient = readme['drugGroup']['conceptGroup'][1]['conceptProperties'][0]['name']
                df.loc[index, 'ingredients'] = ingredient
            except:
                pass
        else:
            time.sleep(1)
            counter = 0
            drug = row['drugname']
            response = requests.get('https://rxnav.nlm.nih.gov/REST/drugs.json?name={}'.format(drug), headers=headers)
            readme = json.loads(response.text)
            try:
                ingredient = readme['drugGroup']['conceptGroup'][1]['conceptProperties'][0]['name']
                df.loc[index, 'ingredients'] = ingredient
            except:
                pass

    df.to_csv('output.csv', index=False)
    print('Fin')

if __name__ == '__main__':
    main()