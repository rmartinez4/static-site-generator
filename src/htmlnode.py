class HTMLNode():
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list[HTMLNode] | None = None, 
        props: dict[str, str] | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        result = ""
        if self.props is not None:
            for p in self.props:
                result += f'{p}="{self.props[p]}" '
        return result.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        props: dict[str, str] | None = None
    ):
        super(LeafNode, self).__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is missing")

        if self.tag is None:
            return self.value

        if self.props is not None:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None, 
        children: str | None, 
        props: dict[str, str] | None = None,
    ):
        super(ParentNode, self).__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing")

        if self.children is None:
            raise ValueError("Parent node has no children")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()

        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"

        return f"<{self.tag}>{children_html}</{self.tag}>"
