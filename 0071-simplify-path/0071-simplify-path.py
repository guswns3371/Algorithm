class Solution:
    def simplifyPath(self, path: str) -> str:
        q = []
        for directory in path.split("/"):
            if directory == ".":
                pass
            elif directory == "..":
                if q:
                    q.pop()
            elif directory != "":
                q.append(directory)
        return "/" + "/".join(q)
