__author__ = 'santiago'

import requests
import json


class RestClientError(Exception):

    def __init__(self, status_code):
        self.status_code = status_code

    def __str__(self):
        return self.status_code, " ", self.message


class RestClient(object):

    def __init__(self, url):
        self.url = url

    def get_tasks(self):
        response = requests.get(self.url+"tasks")
        if response.status_code == requests.codes.ok:
            return response.json()['tasks']
        else:
            raise RestClientError(response.status_code)

    def get_task(self, id):
        response = requests.get(self.url+"tasks/"+str(id))
        if response.status_code == requests.codes.ok:
            return response.json()
        elif response.status_code == requests.codes.not_found:
            return None

    def create_task(self, description):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        data = {"description": description}
        response = requests.post(self.url+"tasks", data=json.dumps(data), headers=headers)
        if response.status_code == requests.codes.created:
            return response.json()['task_id']
        else:
            raise RestClientError(response.status_code)

    def remove_task(self, task_id):
        response = requests.delete(self.url+"tasks/"+str(task_id))
        return response.status_code == requests.codes.no_content

    def modify_task(self, task_id, description=None, status=None):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        data = {}
        if description is not None:
            data['description'] = description
        if status is not None:
            data['status'] = status
        response = requests.put(self.url+"tasks/"+str(task_id), data=json.dumps(data), headers=headers)
        return response.status_code == requests.codes.no_content



if __name__ == "__main__":
    rc = RestClient("http://localhost:9090/")
    tasks = rc.get_tasks()
    print "Initial Tasks:  ", tasks

    task_id = rc.create_task("Test Rest client")
    print "Created task Id: ", task_id

    modified = rc.modify_task(task_id, description="Test Rest Client Modified", status=1)
    if modified:
        task_modified = rc.get_task(task_id)
        print "Task modified: ", task_modified
    else:
        print "task no modified"

    removed = rc.remove_task(task_id)
    if removed:
        tasks = rc.get_tasks()
        print "Final tasks:",  tasks
    else:
        print "Task %s cannot be removed" % task_id
