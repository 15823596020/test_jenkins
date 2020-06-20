import jenkins


class TestJenkins:
    def test_jenkins1(self):
        server = jenkins.Jenkins("http://106.53.247.164:8080/", username="test1", password="test1")
        server.build_job("demo2_node_git")
