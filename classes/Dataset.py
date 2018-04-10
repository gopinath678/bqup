from util import run

class Dataset:

  objects = []

  def __init__ (self, project, name):
    self.project = project
    self.name = name
    project.datasets.append(self)

  @classmethod
  def list(cls, project):
    return list(map(
      lambda name: Dataset(project, name),
      run("bq ls --project_id %s"%(project.name)).split()[2:]
    ))
