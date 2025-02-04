class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [p for p in path.split("/") if p]
        q = []
        for directory in directories:
            if directory == ".":
                continue
            if directory == "..":
                if q:
                    q.pop()
                continue
            q.append(directory)
        return "/" + "/".join(q)
