# import unittest
# from collections import OrderedDict
#
# from bot.bencoding import Decoder, Encoder, BencodingError
#
#
# class DecodingTests(unittest.TestCase):
#
#     def test_integer(self):
#         res = Decoder(b'i123e').decode()
#         self.assertEqual(int(res), 123)
#
#     def test_string(self):
#         res = Decoder(b'4:name').decode()
#         self.assertEqual(res, b'name')
#
#     def test_min_string(self):
#         res = Decoder(b'1:a').decode()
#         self.assertEqual(res, b'a')
#
#     def test_string_with_space(self):
#         res = Decoder(b'12:Middle Earth').decode()
#         self.assertEqual(res, b'Middle Earth')
#
#     def test_empty_string(self):
#         with self.assertRaises(BencodingError):
#             Decoder(b'').decode()
#
#     def test_list(self):
#         res = Decoder(b'l4:spam4:eggsi123ee').decode()
#         self.assertEqual(len(res), 3)
#         self.assertEqual(res[0], b'spam')
#         self.assertEqual(res[1], b'eggs')
#         self.assertEqual(res[2], 123)
#
#     def test_dict(self):
#         res = Decoder(b'd3:cow3:moo4:spam4:eggse').decode()
#         self.assertTrue(isinstance(res, dict))
#         self.assertEqual(res[b'cow'], b'moo')
#         self.assertEqual(res[b'spam'], b'eggs')
#
#     def test_malformed_key_in_dict_should_failed(self):
#         with self.assertRaises(BencodingError):
#             Decoder(b'd3:moo4:spam4:eggse').decode()
#
#
# class EncodingTests(unittest.TestCase):
#
#     def test_empty_encoding(self):
#         res = Encoder(None).encode()
#         self.assertEqual(res, None)
#
#     def test_integer(self):
#         res = Encoder(123).encode()
#         self.assertEqual(b'i123e', res)
#
#     def test_string(self):
#         res = Encoder('Middle Earth').encode()
#         self.assertEqual(b'12:Middle Earth', res)
#
#     def test_bytes(self):
#         res = Encoder(b'Middle Earth').encode()
#         self.assertEqual(b'12:Middle Earth', res)
#
#     def test_list(self):
#         res = Encoder(['spam', 'eggs', 123]).encode()
#         self.assertEqual(b'l4:spam4:eggsi123ee', res)
#
#     def test_dict(self):
#         d = OrderedDict()
#         d['cow'] = 'moo'
#         d['spam'] = 'eggs'
#         res = Encoder(d).encode()
#         self.assertEqual(b'd3:cow3:moo4:spam4:eggse', res)
#
#     def test_nested_structure(self):
#         outer = OrderedDict()
#         b = OrderedDict()
#         b['ba'] = 'foo'
#         b['bb'] = 'bar'
#         outer['a'] = 123
#         outer['b'] = b
#         outer['c'] = [['a', 'b'], 'z']
#         res = Encoder(outer).encode()
#         self.assertEqual(res, b'd1:ai123e1:bd2:ba3:foo2:bb3:bare1:cll1:a1:be1:zee')
#
#
# if __name__ == '__main__':
#     unittest.main()
