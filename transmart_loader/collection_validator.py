from typing import List

from transmart_loader.collection_visitor import CollectionVisitor
from transmart_loader.console import Console
from transmart_loader.loader_exception import LoaderException
from transmart_loader.transmart import TreeNode, DataCollection, Observation,\
    Patient, Visit, TrialVisit, Study, Concept


class CollectionValidator(CollectionVisitor):
    """
    Validation class for TranSMART data collections.
    """

    def visit_concept(self, concept: Concept) -> None:
        pass

    def visit_study(self, study: Study) -> None:
        pass

    def visit_trial_visit(self, trial_visit: TrialVisit) -> None:
        pass

    def visit_visit(self, visit: Visit) -> None:
        pass

    def visit_patient(self, patient: Patient) -> None:
        pass

    def visit_observation(self, observation: Observation) -> None:
        pass

    def visit_node(self, node: TreeNode) -> None:
        if node.parent is not None:
            self.errors.append(
                'Node {} is not a root node'.format(node.name))

    def __init__(self):
        self.errors: List[str] = []

    @staticmethod
    def validate(collection: DataCollection):
        validator = CollectionValidator()
        validator.visit(collection)
        if len(validator.errors) is not 0:
            for error in validator.errors:
                Console.error(error)
            raise LoaderException('Invalid collection')