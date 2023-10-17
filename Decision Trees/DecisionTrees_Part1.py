import math
import sys

categories = []
data = []

with open("mushroom.csv") as f:
    count = 0
    for line in f:
        line = line.strip()
        if count == 0:
            categories = line.split(",")
            count += 1
        else:
            temp = line.split(",")
            row = {}
            for i in range(0, len(categories)):
                row[categories[i]] = temp[i]
            data.append(row)
    
def calculate_entropy(data, categories):
    outcomes = {}
    outcome_category = categories[-1]
    for row in data:
        if row[outcome_category] not in outcomes:
            outcomes[row[outcome_category]] = 1
        else:
            outcomes[row[outcome_category]] += 1
    entropy = 0
    for outcome in outcomes:
        entropy -= (outcomes[outcome]/len(data)) * math.log((outcomes[outcome]/len(data)), 2)
    return entropy

def calculate_information_gain(feature, data):
    poss_values = {}
    for row in data:
        if row[feature] not in poss_values:
            poss_values[row[feature]] = [row]
        else:
            poss_values[row[feature]].append(row)
    entropy = 0
    for val in poss_values:
        entropy += (len(poss_values[val])/len(data)) * calculate_entropy(poss_values[val], categories)
    info_gain = calculate_entropy(data, categories) - entropy
    return info_gain

def generate_tree(tree, data, categories):
    bestFeature = ""
    highestInfoGain = 0
    temp = categories[:-1]
    for feature in temp:
        info_gain = calculate_information_gain(feature, data)
        if info_gain > highestInfoGain:
            highestInfoGain = info_gain
            bestFeature = feature
    tree[bestFeature] = {}
    poss_values = {}
    for row in data:
        if row[bestFeature] not in poss_values:
            poss_values[row[bestFeature]] = [row]
        else:
            poss_values[row[bestFeature]].append(row)
    for val in poss_values:
        tree[bestFeature][val] = {}
        if calculate_entropy(poss_values[val], categories) == 0:
            tree[bestFeature][val] = poss_values[val][0][categories[-1]]
        else:
            generate_tree(tree[bestFeature][val], poss_values[val], categories)        
    return tree

tree = {}
tree = generate_tree(tree, data, categories)

f = open("treeout.txt", "w")
f.close()
f = open("treeout.txt", "a")

def print_tree(tree, data, categories, indent=0):
    for key, value in tree.items():
        print("\t" * indent + "* " + str(key), end="")
        f.write("\t" * indent + "* " + str(key))
        if isinstance(value, dict):
            print()
            f.write("\n")
            print_tree(value, data, categories, indent+1)
        else:
            print(" --> " + str(value))
            f.write(" --> " + str(value + "\n"))
    
print_tree(tree, data, categories)
f.close()