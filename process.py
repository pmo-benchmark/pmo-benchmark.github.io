import pandas as pd
import os 
from collections import defaultdict 
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

sheet_names = ['AUC Top-100', 'AUC Top-10', 'AUC Top-1', 'Top-100', 'Top-10', 'Top-1', ]

result_dict = defaultdict(lambda:defaultdict(lambda:defaultdict()))
for sheet_name in sheet_names:
	df = pd.read_excel(file_path, sheet_name=sheet_name)
	methods = df.columns.to_list()[1:] ## 'screening', 'mol_pal', 
	properties = df.iloc[:, 0].to_list()[:-2] 
	for i,method in enumerate(methods):
		for j,prop in enumerate(properties): 
			result_dict[prop][method][sheet_name] = float(df.iloc[j,i+1])


with open('_layouts/tmp1.html') as fin:
	lines1 = fin.readlines() 
lines1[-1] = lines1[-1].strip()

with open('_layouts/tmp2.html') as fin:
	lines2 = fin.readlines() 
lines2[-1] = lines2[-1].strip()


for prop in properties:
	if not os.path.exists(prop):
		os.makedirs(prop)
	file = os.path.join(prop, 'index.md') 
	with open(file, 'w') as fo:
		fo.write('---\n')
		fo.write('layout: '+ prop + '\n')
		fo.write('title: "PMO: ' + prop + '"\n')
		fo.write("permalink: /"+ prop +'\n\n')
		fo.write('---\n\n')
		fo.write('# ' + prop + " Leaderboard\n")
		fo.write('\n\n\n\n')
		fo.write('| Method | AUC top-100 | AUC top-10 | AUC top-1 | top-100 | top-10 | top-1 |\n')
		fo.write('| :--- | :------------- | :--- | :--- | :--- | :--- | :--- |\n')
		result_list = []
		for method in methods:
			lst = [method,]+ [result_dict[prop][method][sheet_name] for sheet_name in sheet_names] 
			result_list.append(lst)
		result_list = sorted(result_list, key=lambda x:x[2], reverse=True)
		for result in result_list:
			fo.write('| ' + result[0] + ' | ' + ' | '.join([str(i)[:5] for i in result[1:]]) + ' |\n')
		fo.write('\n\n')
	file = os.path.join('_layouts', prop+'.html')
	with open(file, 'w') as fo:
		for line in lines1:
			fo.write(line)
		fo.write(prop)
		for line in lines2: 
			fo.write(line)



print('\n\n##### _layouts/default.html ####\n\n')
for prop in properties:
	print('      <a href="' + prop + '.html" class="btn">' + prop + '</a>')









