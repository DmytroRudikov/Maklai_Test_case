from nltk import Tree
from typing import List
import itertools


class Paraphrase:

    def __init__(self, tree_str: str):
        self.labels_to_swap = []
        self.tree_positions = []
        self.paraphrase_list = []
        self.tree = Tree.fromstring(tree_str)

    def tree_parsing(self):
        for position in self.tree.treepositions():
            try:
                if self.tree[position].label() == "NP":
                    label_list = [sub_t.label() for sub_t in self.tree[position]]
                    if label_list.count("NP") > 1:
                        label_indices = tuple(i for i in range(len(label_list)) if label_list[i] == "NP")
                        self.labels_to_swap.append(label_indices)
                        self.tree_positions.append(position)
            except AttributeError:
                continue

    def rephrase_algorythm(self, all_possible_combinations: List[list], next_index: int = 0):
        for item_index in range(next_index, len(all_possible_combinations)):
            next_index += 1
            item = all_possible_combinations[item_index]
            for i in range(len(item)):
                if item[i] == self.labels_to_swap[item_index]:
                    if item_index != len(all_possible_combinations) - 1:
                        self.rephrase_algorythm(all_possible_combinations, next_index)
                else:
                    tree_copy = self.tree.copy(deep=True)
                    for n in range(len(item[i])):
                        if item[i][n] != self.labels_to_swap[item_index][n]:
                            tree_copy[self.tree_positions[item_index]][self.labels_to_swap[item_index][n]] = \
                            self.tree[self.tree_positions[item_index]][item[i][n]]
                    tree_copy_str = " ".join(str(tree_copy).split())
                    dict_to_append = {"tree": tree_copy_str}
                    self.paraphrase_list.append(dict_to_append)

    def rephrase(self) -> List[dict]:
        self.tree_parsing()
        permutation_objects = [itertools.permutations(i) for i in self.labels_to_swap]
        all_possible_combinations = [[e for e in i] for i in permutation_objects]
        self.rephrase_algorythm(all_possible_combinations=all_possible_combinations)
        return self.paraphrase_list
