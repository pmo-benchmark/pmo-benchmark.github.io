import pandas as pd
import os 
file_path = "Mol_Opt.xlsx"
xl = pd.ExcelFile(file_path)
sheet_names = xl.sheet_names
print(sheet_names)
# ['AUC Top-100', 'Models', 'Oracles', 'AUC final', 'Ranking', 
#  'Top-1', 'Top-10', 'Top-100', 'AUC Top-1', 'AUC Top-10', 'AUC Top-10 std', 
#  'AUC Top-1 std', 'auctop100 std', 'top1_std', 'top10_std', 'top100_std']

properties = ['albuterol_similarity', 'amlodipine_mpo', 'celecoxib_rediscovery', \
				'deco_hop', 'drd2', 'fexofenadine_mpo', 'gsk3b', 'isomers_c7h8n2o2', \
				'isomers_c9h10n2o2pf2cl', 'jnk3', 'median1', 'median2', 'mestranol_similarity', \
				'osimertinib_mpo', 'perindopril_mpo', 'qed', 'ranolazine_mpo', 'scaffold_hop', \
				'sitagliptin_mpo', 'thiothixene_rediscovery', 'troglitazone_rediscovery',\
				'valsartan_smarts', 'zaleplon_mpo', ]

sheet_names = ['AUC Top-100', 'Top-1', 'Top-10', 'Top-100', 'AUC Top-1', 'AUC Top-10', ]

for sheet_name in sheet_names:
	df = pd.read_excel(file_path, sheet_name=sheet_name)
	methods = df.columns.to_list()[1:] ## 'screening', 'mol_pal', 
	properties = df.iloc[:, 0].to_list()[:-2] 
	print(properties, methods)
	print(len(properties), len(methods))

print(len(properties), properties)


