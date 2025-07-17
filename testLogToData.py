import unittest
from logToData import lineToRecord, extractField

class TestLineToRecord(unittest.TestCase):

    ### TESTS FOR extractField() ###

    def test_extract_from_start(self):
        result = extractField("hello world", 0, " ")

        self.assertEqual(result[0], "hello")
        self.assertEqual(result[1], 5)
    
    def test_extract_from_point(self):
        result = extractField("hello world", 2, " ")

        self.assertEqual(result[0], "llo")
        self.assertEqual(result[1], 5)
    
    def test_extract_run_off(self):
        result = extractField("hello world", 7, " ")

        self.assertEqual(result[0], "orld")
        self.assertEqual(result[1], 11)
    
    def test_extract_out_bound(self):
        result = extractField("hello world", 100, " ")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], 100)
    
    def test_extract_negative_index(self):
        result = extractField("hello world", -1, " ")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], 0)
    
    def test_extract_on_stop(self):
        result = extractField("hello world", 5, " ")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], 5)
    
    def test_extract_all_stop(self):
        result = extractField("        ", 0, " ")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], 0)
    
    def test_extract_no_stop(self):
        result = extractField("hello world", 0, "")

        self.assertEqual(result[0], "hello world")
        self.assertEqual(result[1], 11)
    
    def test_extract_string_stop(self):
        result = extractField("hello world go goodbye", 0, " goo")

        self.assertEqual(result[0], "hello")
        self.assertEqual(result[1], 5)
    
    def test_extract_empty_line(self):
        result = extractField("", 0, " ")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], 0)



    ### TESTS FOR lineToRecord() ###

    def test_default(self):
        result = lineToRecord("100.34.17.233 - NO - [01/07/2025:06:00:02] \"GET /news/grammy-nominations-2024 HTTP/1.1\" 302 1234 \"-\" \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\" 269")
        
        self.assertEqual(result[0], "100.34.17.233")
        self.assertEqual(result[1], "NO")
        self.assertEqual(result[2], "01/07/2025:06:00:02")
        self.assertEqual(result[3], "GET")
        self.assertEqual(result[4], "\"/news/grammy-nominations-2024 HTTP/1.1\"")
        self.assertEqual(result[5], "302")
        self.assertEqual(result[6], "1234")
        self.assertEqual(result[7], "-")
        self.assertEqual(result[8], "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\"")
        self.assertEqual(result[9], "269")
    
    def test_incomplete(self):
        result = lineToRecord("100.34.17.233 - NO - [01/07/2025:06:00:02] \"GET /news/grammy-nominations-2024")
        
        self.assertEqual(result[0], "100.34.17.233")
        self.assertEqual(result[1], "NO")
        self.assertEqual(result[2], "01/07/2025:06:00:02")
        self.assertEqual(result[3], "GET")
        self.assertEqual(result[4], "\"/news/grammy-nominations-2024\"")
        self.assertEqual(result[5], "")
        self.assertEqual(result[6], "")
        self.assertEqual(result[7], "")
        self.assertEqual(result[8], "\"\"")
        self.assertEqual(result[9], "")
    
    def test_empty_log(self):
        result = lineToRecord("")

        self.assertEqual(result[0], "")
        self.assertEqual(result[1], "")
        self.assertEqual(result[2], "")
        self.assertEqual(result[3], "")
        self.assertEqual(result[4], "\"\"")
        self.assertEqual(result[5], "")
        self.assertEqual(result[6], "")
        self.assertEqual(result[7], "")
        self.assertEqual(result[8], "\"\"")
        self.assertEqual(result[9], "")


# Run unit tests
if __name__ == '__main__':
    unittest.main()
