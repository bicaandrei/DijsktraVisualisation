from domain.Nodes import Node
from repositories.repository_nodes import RepoNodes
from repositories.repository_lines import RepoLines
from services.service_nodes import ServiceNodes
from services.service_lines import ServiceLines
from ui.user_interface import UI

def main():

    repository_nodes = RepoNodes()
    repository_lines = RepoLines()
    service_nodes = ServiceNodes(repository_nodes)
    service_lines = ServiceLines(repository_lines)

    console = UI(service_nodes, service_lines, 800, 800)
    console.run()


main()