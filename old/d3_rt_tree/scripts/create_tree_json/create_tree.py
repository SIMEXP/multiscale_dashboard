import json
import os
import pickle

def main():

	project_path = os.getcwd() 
	pickle_filepath = project_path + "/data/pickle_dict_pt3.p"
	trees_list = pickle.load(open(pickle_filepath, "rb"))
	
	output_dict = {}
	for index in range(len(trees_list)):
		
		current_tree_filepath = "/data/tree_roi_{0}.json".format(trees_list[index]["roi"])
		
		# [u'roi', u'name', u'symmetry', u'laterality', u'overlap', u'label', 
		#  u'Neighbours', u'COM', u'Children', u'size']
		output_dict[trees_list[index]["roi"]] = {}
		for key in trees_list[index]:
			output_dict[trees_list[index]["roi"]][key] = trees_list[index][key]
			
		with open(project_path + current_tree_filepath, "w") as json_file:
			print "Writing {0}".format(project_path + current_tree_filepath)
			json.dump(output_dict, json_file)
			

if "__main__" == __name__:
	main()