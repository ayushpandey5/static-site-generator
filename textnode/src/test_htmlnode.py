import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("a","google",None,{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a","boot.dev",None,{"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

if __name__ == "__main__":
    unittest.main()