


file_legacy = open('data/legacy.txt', 'r')
legacies = []
export = {}
for line in file_legacy: 
	if "------" in line:
		if 'id' not in export:
			export['id'] = -1
		if 'pattern' not in export:
			export['pattern'] = ""
		if 'collection' not in export:
			export['collection'] = ""
		if 'restriction' not in export:
			export['restriction'] = ""
		if 'filters' not in export:
			export['filters'] = []
		if 'basket_id' not in export:
			export['basket_id'] = ""	
		legacies.append(export)
		export = {}
	if "legacy id " in line:
		export['id'] = int(line.replace("legacy id ", ""))
	elif "search_pattern : " in line:
		export['pattern'] = line.replace("search_pattern : ", "")
	elif "search_collection : " in line:
		export['collection'] = line.replace("search_collection : ", "")
	elif "search_field_restriction : " in line:
		export['restriction'] = line.replace("search_field_restriction : ", "")
	elif "search_filter : " in line:
		export['filters'] = line.replace("search_filter : ", "").split(",")
	elif "search_basket_id : " in line:
		export['basket_id'] = int(line.replace("search_basket_id : ", ""))

file_legacy.close()



file_people = open('data/people.txt', 'r')
ids = []
people_curator = 0
people_other = 0
for line in file_people: 
	if "https://infoscience.epfl.ch/curator/export/" in line or "http://infoscience.epfl.ch/curator/export/" in line:
		digit = line.split("/")[5]
		if digit.isdigit():
			people_curator += 1
			ids.append(int(digit))
		else:
			people_other += 1
	elif "https://infoscience.epfl.ch/curator/publications/exporter/" in line or "http://infoscience.epfl.ch/curator/publications/exporter/" in line:
		people_curator += 1
		ids.append(int(line.split("/")[6]))
	else:
		people_other += 1
file_people.close()



file_jahia = open('data/jahia.txt', 'r')
jahia_curator = 0
jahia_other = 0
for line in file_jahia:
	if "https://infoscience.epfl.ch/curator/export/" in line or "http://infoscience.epfl.ch/curator/export/" in line:
		digit = line.split("/")[5]
		if digit.isdigit():
			jahia_curator += 1
			ids.append(int(digit))
		else:
			jahia_other += 1
	elif "https://infoscience.epfl.ch/curator/publications/exporter/" in line or "http://infoscience.epfl.ch/curator/publications/exporter/" in line:
		jahia_curator += 1
		ids.append(int(line.split("/")[6]))
	else:
		jahia_other += 1
file_jahia.close()


counter_none = 0   # should be impossible => always 0
counter_basket = 0
counter_pattern = 0
counter_collection = 0
counter_restriction = 0
counter_filters = 0
counter_pattern_collection = 0
counter_pattern_restriction = 0
counter_pattern_filters = 0
counter_collection_restriction = 0
counter_collection_filters = 0
counter_restriction_filters = 0
counter_pattern_collection_restriction = 0
counter_pattern_collection_filters = 0
counter_pattern_restriction_filters = 0
counter_collection_restriction_filters = 0
counter_pattern_collection_restriction_filters = 0
filters = {}
nones_id = []

for id_ in ids:
	for legacy in legacies:
		if legacy['id'] == id_:
			if legacy['basket_id']:
				counter_basket += 1
			elif legacy['pattern']:
				if legacy['collection']:
					if legacy['restriction']:
						if legacy['filters']:
							counter_pattern_collection_restriction_filters += 1
						else:
							counter_pattern_collection_restriction += 1
					else:
						if legacy['filters']:
							counter_pattern_collection_filters += 1
						else:
							counter_pattern_collection += 1
				else:
					if legacy['restriction']:
						if legacy['filters']:
							counter_pattern_restriction_filters += 1
						else:
							counter_pattern_restriction += 1
					else:
						if legacy['filters']:
							counter_pattern_filters += 1
						else:
							counter_pattern += 1
			else:
				if legacy['collection']:
					if legacy['restriction']:
						if legacy['filters']:
							counter_collection_restriction_filters += 1
						else:
							counter_collection_restriction += 1
					else:
						if legacy['filters']:
							counter_collection_filters += 1
						else:
							counter_collection += 1
				else:
					if legacy['restriction']:
						if legacy['filters']:
							counter_restriction_filters += 1
						else:
							counter_restriction += 1
					else:
						if legacy['filters']:
							counter_filters += 1
						else:
							counter_none += 1
							nones_id.append(id_)
					
			for filter_ in legacy['filters']:
				if filter_ in filters:
					filters[filter_] = filters[filter_] + 1
				else:
					filters[filter_] = 1


file_results = open('results/group_counter_results.txt', 'w')

file_results.write("=================\n")
file_results.write("PEOPLE :\n")
file_results.write("curator = " + str(people_curator) +"\n")
file_results.write("other = " + str(people_other) +"\n")
file_results.write("=================\n")
file_results.write("JAHIA :\n")
file_results.write("curator = " + str(jahia_curator) +"\n")
file_results.write("other = " + str(jahia_other) +"\n")
file_results.write("=================\n")
file_results.write("none = " + str(counter_none) +"\n")
file_results.write("basket = " + str(counter_basket) +"\n")
file_results.write("pattern = " + str(counter_pattern) +"\n")
file_results.write("collection = " + str(counter_collection) +"\n")
file_results.write("restriction = " + str(counter_restriction) +"\n")
file_results.write("filters = " + str(counter_filters) +"\n")
file_results.write("pattern_collection = " + str(counter_pattern_collection) +"\n")
file_results.write("pattern_restriction = " + str(counter_pattern_restriction) +"\n")
file_results.write("pattern_filters = " + str(counter_pattern_filters) +"\n")
file_results.write("collection_restriction = " + str(counter_collection_restriction) +"\n")
file_results.write("collection_filters = " + str(counter_collection_filters) +"\n")
file_results.write("restriction_filters = " + str(counter_restriction_filters) +"\n")
file_results.write("pattern_collection_restriction = " + str(counter_pattern_collection_restriction) +"\n")
file_results.write("pattern_collection_filters = " + str(counter_pattern_collection_filters) +"\n")
file_results.write("pattern_restriction_filters = " + str(counter_pattern_restriction_filters) +"\n")
file_results.write("collection_restriction_filters = " + str(counter_collection_restriction_filters) +"\n")
file_results.write("pattern_collection_restriction_filters = " + str(counter_pattern_collection_restriction_filters) +"\n")

file_results.write("=================\n")
file_results.write("FILTERS :\n")
for key, value in filters.items():
	file_results.write(key + " = " + str(value) + "\n")

file_results.write("=================\n")
file_results.write("NONE :\n")
for none_id in nones_id:
	file_results.write("https://infoscience.epfl.ch/curator/export/" + str(none_id) + "\n")

file_results.close()

					
		
