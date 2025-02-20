import unittest
from htmlnode import LeafNode, HTMLNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="p", value="This is the text")
        node2 = LeafNode(tag="p", value="This is the text")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = LeafNode(tag="p", value="This is the text")
        node2 = LeafNode(tag="b", value="BOLD TEXT")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = LeafNode(tag="i", value="This is the italic text")
        node2 = LeafNode(tag="b", value="This is the bold text")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = LeafNode(tag="a", value="This is the url text", props=dict(href="https://laernorsk.no"))
        node2 = LeafNode(tag="a", value="This is the url text", props=dict(href="https://laernorsk.no"))
        self.assertEqual(node, node2)

    def test_repr(self):
        node = LeafNode(tag="a", value="This is the url text", props=dict(href="https://laernorsk.no"))
        self.assertEqual(
            "LeafNode(a, This is the url text, {'href': 'https://laernorsk.no'})", repr(node)
        )

    def test_to_html_with_url(self):
        node = LeafNode(tag="a", value="This is the url text", props=dict(href="https://laernorsk.no"))
        self.assertEqual(
            '<a href="https://laernorsk.no">This is the url text</a>', node.to_html()
        )

    def test_to_html(self):
        node = LeafNode(tag="p", value="This is the paragraph text")
        self.assertEqual(
            '<p>This is the paragraph text</p>', node.to_html()
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, value="This is the paragraph text")
        self.assertEqual(
            'This is the paragraph text', node.to_html()
        )


if __name__ == "__main__":
    unittest.main()
