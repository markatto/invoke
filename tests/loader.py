import os
import sys

from spec import Spec, skip, eq_, raises

from invoke.loader import Loader
from invoke.collection import Collection
from invoke.exceptions import CollectionNotFound

from _utils import support


class Loader_(Spec):
    def exposes_discovery_root(self):
        root = '/tmp/'
        eq_(Loader(root=root).root, root)

    def has_a_default_discovery_root(self):
        eq_(Loader().root, os.getcwd())

    class load_collection:
        def returns_collection_object_if_name_found(self):
            result = Loader(root=support).load_collection('foo')
            eq_(type(result), Collection)

        @raises(CollectionNotFound)
        def raises_CollectionNotFound_if_not_found(self):
            Loader(root=support).load_collection('nope')

        def raises_InvalidCollection_if_invalid(self):
            skip()

        def honors_discovery_root_option(self):
            skip()

        def searches_towards_root_of_filesystem(self):
            skip()

        def only_adds_valid_task_objects(self):
            skip()

        def adds_actual_tasks_not_just_task_bodies(self):
            skip()

        def adds_valid_subcollection_objects(self):
            skip()

        def defaults_to_tasks_collection(self):
            "defaults to 'tasks' collection"
            result = Loader(root=support + '/implicit/').load_collection()
            eq_(type(result), Collection)

    class add_to_collection:
        @raises(CollectionNotFound)
        def raises_CollectionNotFound_for_missing_collections(self):
            c = Collection()
            result = Loader(root=support).add_to_collection('nope', c)

    class load:
        def returns_nested_collection_from_all_given_names(self):
            skip()

        def uses_first_collection_as_root_namespace(self):
            skip()

        def raises_CollectionNotFound_if_any_names_not_found(self):
            skip()

        def raises_InvalidCollection_if_any_found_modules_invalid(self):
            skip()

    class update_path:
        def setup(self):
            self.l = Loader(root=support)

        def does_not_modify_argument(self):
            path = []
            new_path = self.l.update_path(path)
            eq_(path, [])
            assert len(new_path) > 0

        def inserts_self_root_parent_at_front_of_path(self):
            "Inserts self.root at front of path"
            eq_(self.l.update_path([])[0], self.l.root)

        def does_not_insert_if_exists(self):
            "Doesn't insert self.root if it's already in the path"
            new_path = self.l.update_path([self.l.root])
            eq_(len(new_path), 1) # not 2
