#! /usr/bin/env python

import executor


class Archiver(executor.Executor):

    def archive(self):
        self.logger.info("Archiving")
        self.ds.safe_archive_all(int(self.config.archive_threshold))


if __name__ == "__main__":
    Archiver().archive()
