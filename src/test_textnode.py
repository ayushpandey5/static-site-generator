import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node1_1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Test node", TextType.CODE, "www.google.com")
        node2_1 = TextNode("Test node", TextType.CODE, "www.google.com")
        node3 = TextNode("Test node", TextType.IMAGE, "www.google.com")
        node3_1 = TextNode("Test node", TextType.LINK, "www.google.com")
        self.assertEqual(node1, node1_1)
        self.assertEqual(node2, node2_1)
        self.assertNotEqual(node3, node3_1)




if __name__ == "__main__":
    unittest.main()