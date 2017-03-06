from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    @task
    def page1(self):
        self.client.get("/sugestoes-para/6a-feira-da-quarta-semana-da-pascoa/")

    @task
    def page2(self):
        self.client.get("/sugestoes-para/5a-feira-da-quarta-semana-da-pascoa/")

    @task
    def page3(self):
        self.client.get("/sugestoes-para/4a-feira-da-quarta-semana-da-pascoa/")

    @task
    def page4(self):
        self.client.get("/sugestoes-para/3a-feira-da-quarta-semana-da-pascoa/")

    @task
    def musica1(self):
        self.client.get("/musica/ressuscitou/")

    @task
    def musica2(self):
        self.client.get("/musica/prova-de-amor-maior-nao-ha/")

    @task
    def musica3(self):
        self.client.get("/musica/porque-ele-vive/")

    @task
    def musica4(self):
        self.client.get("/musica/o-senhor-ressuscitou-aleluia/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
