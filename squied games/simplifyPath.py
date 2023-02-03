class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for name in path:
            if len(name) == 0 or name == ".":
                continue
                
            if name == "..":
                if stack: stack.pop()
                continue
            stack.append(name)
        return "/" + "/".join(stack)
