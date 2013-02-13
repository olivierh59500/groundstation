import os
import pygit2

import groundstation.logger
log = groundstation.logger.getLogger(__name__)

class GitStore(object):
    required_dirs = ("rindex", "grefs")
    def __init__(self, path):
        # TODO path should probably be a resource, ie redis url etc.
        self.path = path
        if not os.path.exists(os.path.join(path, "objects")):
            log.info("initializing database in %s" % (path))
            pygit2.init_repository(path, True)
        self.repo = pygit2.Repository(path)
        self.check_repo_sanity()

    def objects(self):
        return list(self.repo)

    def __getitem__(self, key):
        return self.repo[unicode(key)]

    def __contains__(self, item):
        return unicode(item) in self.repo

    def lookup_reference(self, ref):
        return self.repo.lookup_reference(ref)

    def write(self, typ, data):
        return self._format_id(self.repo.write(typ, data))

    def create_blob(self, data):
        return self._format_id(self.repo.create_blob(data))

    def create_reference(self, ref, data):
        return self.repo.create_reference(ref, data)

    @staticmethod
    def _format_id(obj_id):
        return "".join(["%02x" % ord(i) for i in obj_id])

    def gref_path(self, path):
        return os.path.join(self.repo.path, "grefs", path)

    def rindex_path(self, path):
        return os.path.join(self.repo.path, "reindex", path)

    def check_repo_sanity(self):
        for path in self.required_dirs:
            nr_path = os.path.join(self.repo.path, path)
            if not os.path.exists(nr_path):
                os.makedirs(nr_path)
