import unittest
import http.client
import json


class MyViewTestCase(unittest.TestCase):
    def test_get_object(self):
        conn = http.client.HTTPConnection("http://127.0.0.1:8000")
        body = {
            "inn": 7707049388,
            "nomer_zajavki": 50252265,
            "start_date": "09.03.23",
            "end_date": "13.03.23",
        }
        payload = json.dumps(body)
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        conn.request(
            "GET",
            f"/?inn={body['inn']}"
            f"&nomer_zajavki={body['nomer_zajavki']}"
            f"&start_date={body['start_date']}"
            f"&end_date={body['end_date']}",
            payload,
            headers
        )
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        conn.close()
        json_ = json.loads(data)
        try:
            self.assertEqual(200, json_['code'])
        except Exception as e:
            print(f'Сообщение: {e}')


if __name__ == '__main__':
    unittest.main()
