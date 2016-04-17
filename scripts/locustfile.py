from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/sugestoes-para/6a-feira-da-quarta-semana-da-pascoa/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
