class AutoComplete:
    def __init__(self, search_terms: [str] = None):
        self.root = {}
        self.fill_trie(search_terms)

    def fill_trie(self, search_terms: [str]):
        for search_term in search_terms:
            term = search_term.lower()
            root = self.root
            for i in range(len(term)):
                char = term[i]
                if char not in root:
                    root[char] = {}
                if i == len(term) - 1:
                    root[char]["$"] = None
                root = root[char]

    def search(self, term: str) -> [str]:
        root = self.root
        for i in range(len(term)):
            char = term[i]
            if char in root:
                root = root[char]
            else:
                return []
        _, results = self._get_rest_of_trie(root=root)
        results = list(map(lambda x: term + x, results))
        return results

    def _get_rest_of_trie(self, root: dict, results: [str] = []) -> (dict, [str]):
        # if empty dict
        if not bool(root):
            return root, results
        new_results = []
        for char, child_trie in root.items():
            if char == "$":
                new_results.append("$")
            else:
                child_root, child_results = self._get_rest_of_trie(root=child_trie, results=results)
                new_results.extend(list(map(lambda x: char + x, child_results)))
        return root, new_results

    def print_trie(self):
        print(self.root)


if __name__ == "__main__":
    search_terms = ["one", "ones", "honest", "only", "on", "oner"]
    search_terms.extend(list(map(lambda x: x[1:], search_terms)))
    autocomplete = AutoComplete(search_terms)
    autocomplete.print_trie()
    search_term = "n"
    print("SEARCH FOR:", search_term)
    [print(search) for search in autocomplete.search(search_term)]
