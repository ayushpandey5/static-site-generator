import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "Link", None,{
            "href" : "www.google.com",
            "name": "Google"})
        props_string = node1.props_to_html()
        
        self.assertEqual(props_string, ' href="www.google.com" name="Google"')

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "Hello", None, {})
        props_string = node.props_to_html()
        self.assertEqual(props_string, "")

if __name__ == "__main__":
    unittest.main()
