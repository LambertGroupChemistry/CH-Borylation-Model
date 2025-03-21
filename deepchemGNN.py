import deepchem as dc
import pandas as pd
import numpy as np
import csv
from rdkit import Chem
from sklearn.metrics import accuracy_score

#Remove those numbers from analysis data
def filter_rows_by_values1(df, col, values):
    return df[~df[col].isin(values)]

#Remove those numbers from analysis data
def filter_rows_by_values2(df, col, values):
    return df[df[col].isin(values)]

# Read Training/Test data input File
data = pd.read_csv('BorylationTrainingTest 1-10-25.csv')

#group the compounds by numbers
data['grouped'] = data.groupby('Substrate', sort=False).ngroup()


for_range = range(1, 11)
for x in for_range:
    #Get numbers to represent compounds
    arr = np.arange(0, 188,  dtype=int)

    #Get 20% of numbers, without replacement
    set_numbers = np.random.choice(arr, int(len(arr)*0.20), replace=False ) 
    
    #Seperate training (80%) and test data (20%)
    training_data = filter_rows_by_values1(data, "grouped", set_numbers)
    training_data = training_data[['Substrate','Product_Ratio']]
   
    reactants = training_data['Substrate']
    reactants_mol_list = []
    for inChi_reactants in reactants:
      reactants_mol = Chem.MolFromInchi(inChi_reactants)
      reactants_mol_list.append(reactants_mol)

    # Puts reactants into Pandas Type
    training_data['mol'] = pd.DataFrame(reactants_mol_list, index=training_data.index)
    training_data = training_data[['mol','Product_Ratio']]
        
    test_data = filter_rows_by_values2(data, "grouped", set_numbers)
    test_data = test_data.drop('grouped', axis = 1)
       
    reactants = test_data['Substrate']
    reactants_mol_list = []
    for inChi_reactants in reactants:
      reactants_mol = Chem.MolFromInchi(inChi_reactants)
      reactants_mol_list.append(reactants_mol)

    # Puts reactants into Pandas Type
    test_data['mol'] = pd.DataFrame(reactants_mol_list, index=test_data.index)
    test_data = test_data[['mol','Product_Ratio']]
    # Convert Product_Ratio column to a NumPy array
    training_PRarray = training_data['Product_Ratio'].to_numpy()
    test_PRarray = test_data['Product_Ratio'].to_numpy()
    featurizer=dc.feat.ConvMolFeaturizer(per_atom_fragmentation=False)
    trainingfeat = featurizer.featurize(training_data['mol'])
    testfeat = featurizer.featurize(test_data['mol'])
    dataset = dc.data.NumpyDataset(trainingfeat, training_PRarray)
    testset = dc.data.NumpyDataset(testfeat, test_PRarray)
    model = dc.models.GraphConvModel(n_tasks=1, mode="classification",batch_normalize=False)
    model.fit(dataset)
    pred = model.predict(testset)
    metric = dc.metrics.Metric(dc.metrics.accuracy_score)
    acc = model.evaluate(testset, [metric])
    df = pd.DataFrame(acc, index=[x])
    df.to_csv('GNN_acc.csv', mode= 'a')

