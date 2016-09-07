# encoding=utf-8

class UserAgentMiddleware(object):

    def process_request(self,request,spider):
        agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        request.headers["User-Agent"] = agent
