# Title: Delete Duplicate Folders in System
# URL: https://leetcode.com/problems/delete-duplicate-folders-in-system/
# Difficulty: Hard

from collections import defaultdict

class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = {}  # map: folder_name (str) -> Node
        self.deleted = False
        self.structure_string = None # Computed during post-order traversal

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        # 1. Build a file system tree
        # Use a dummy root node to represent the conceptual parent of all top-level folders.
        root = Node("") 

        for path_list in paths:
            current_node = root
            for folder_name in path_list:
                if folder_name not in current_node.children:
                    new_node = Node(folder_name)
                    current_node.children[folder_name] = new_node
                current_node = current_node.children[folder_name]

        # 2. Post-order DFS to compute structure strings and identify duplicates
        # structure_to_nodes maps a unique structure string to a list of Node objects
        # that share that structure.
        structure_to_nodes = defaultdict(list)

        def dfs_compute_structure(node: Node) -> None:
            if not node.children: # Leaf node (no subfolders)
                node.structure_string = ""
                # Leaf nodes themselves are not added to structure_to_nodes for direct deletion.
                # They can only be deleted if an ancestor is deleted.
                return
            
            # Collect children's structures, sorted by name for a canonical representation
            child_structures = []
            for child_name in sorted(node.children.keys()):
                child_node = node.children[child_name]
                dfs_compute_structure(child_node) # Recursively compute child's structure
                # Format: (child_name child_structure_string)
                child_structures.append(f"({child_name}{child_node.structure_string})")

            # The structure string for the current node is based on its children's concatenated structures
            node.structure_string = "".join(child_structures)

            # Only consider folders with a non-empty set of subfolders for duplication criteria.
            # If node.structure_string is non-empty, it implies the folder has at least one child.
            if node.structure_string: 
                structure_to_nodes[node.structure_string].append(node)

        dfs_compute_structure(root)

        # 3. Mark folders for deletion
        for s_string, node_list in structure_to_nodes.items():
            if len(node_list) > 1:
                # If multiple folders share the same non-empty structure string,
                # they are identical. Mark them (and their entire subtrees) for deletion.
                for node in node_list:
                    node.deleted = True

        # 4. Collect remaining paths
        result_paths = []
        # Use a list as a stack to build the current path during DFS traversal
        current_path_segments = [] 

        def dfs_collect_paths(node: Node) -> None:
            if node.deleted:
                return # This node and its entire subtree are marked for deletion, so skip

            # If it's not the dummy root, add its path to the results
            if node != root:
                current_path_segments.append(node.name)
                result_paths.append(list(current_path_segments)) # Add a deep copy of the current path

            # Recursively collect paths from children
            # Ensure consistent order for children traversal (important for deterministic behavior,
            # though problem says order does not matter for output).
            for child_name in sorted(node.children.keys()):
                child_node = node.children[child_name]
                dfs_collect_paths(child_node)

            # Backtrack: remove this node's name from current_path_segments
            # This step is performed only if the node's name was added to current_path_segments.
            if node != root:
                current_path_segments.pop()

        dfs_collect_paths(root)
        return result_paths
